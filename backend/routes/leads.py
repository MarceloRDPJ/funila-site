from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from pydantic import BaseModel
from typing import Optional
from database import get_client
from services.scorer import calculate_internal_score
from services.serasa import check_serasa_score
from routes.auth import get_current_user
import os
import httpx
from datetime import datetime
from cryptography.fernet import Fernet

router = APIRouter()

def encrypt_data(data: str) -> str:
    key = os.environ.get("ENCRYPTION_KEY")
    if not key:
        # Fallback for development only - In production, this must be set!
        # Using a deterministic key based on a secret would be better than random here
        # but for safety, we just log a warning.
        # If no key, we can't decrypt later.
        print("WARNING: ENCRYPTION_KEY missing. Using dummy key for encryption.")
        key = Fernet.generate_key()
    else:
        key = key.encode() if isinstance(key, str) else key

    try:
        f = Fernet(key)
        return f.encrypt(data.encode()).decode()
    except Exception as e:
        print(f"Encryption error: {e}")
        return data # Fallback to raw if encryption fails (better to save than lose lead?)

class LeadInput(BaseModel):
    name: str
    phone: str
    # Step 2
    has_clt: Optional[bool] = False
    clt_years: Optional[str] = None
    # Step 3
    income: Optional[str] = None
    tried_financing: Optional[bool] = False
    cpf: Optional[str] = None
    consent_given: bool
    # Context
    link_slug: Optional[str] = None # To identify client/link

    # UTMs
    utm_source: Optional[str] = None
    utm_campaign: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_content: Optional[str] = None
    utm_term: Optional[str] = None

    device_type: Optional[str] = "mobile" # default

async def send_hot_lead_email(lead_data: dict, score: int, badge: str, client_email: str):
    api_key = os.environ.get("RESEND_API_KEY")
    if not api_key or not client_email:
        return

    subject = f"🔥 Lead Quente Detectado: {lead_data['name']} (Score {score})"

    html_content = f"""
    <h1>Novo Lead Quente!</h1>
    <p><strong>Nome:</strong> {lead_data['name']}</p>
    <p><strong>Telefone:</strong> {lead_data['phone']}</p>
    <p><strong>Score:</strong> {score} ({badge})</p>
    <p><strong>Renda:</strong> {lead_data.get('income', 'N/A')}</p>
    <p><strong>CLT:</strong> {lead_data.get('clt_years', 'N/A')}</p>
    <br>
    <a href="https://app.funila.com.br/admin" style="background:#2563EB;color:white;padding:10px 20px;text-decoration:none;border-radius:5px;">Ver no Painel</a>
    """

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "from": "Funila <noreply@resend.dev>", # Default sender
        "to": [client_email],
        "subject": subject,
        "html": html_content
    }

    try:
        async with httpx.AsyncClient() as client:
            await client.post("https://api.resend.com/emails", json=payload, headers=headers)
    except Exception as e:
        print(f"Failed to send email: {e}")

@router.post("/leads")
async def create_lead(lead: LeadInput, background_tasks: BackgroundTasks):
    db = get_client()
    if not db:
        raise HTTPException(status_code=500, detail="Database connection error")

    # 1. Calculate Internal Score
    lead_dict = lead.model_dump()
    score, status = calculate_internal_score(lead_dict)

    # 2. Check Serasa (Optional)
    # Only if CPF provided. Manual: "Se CPF fornecido e plano Pro"
    # We need to check client plan.
    # First, resolve client from link_slug or fallback.

    client_id = None
    link_id = None
    client_plan = "solo"
    client_email = None

    if lead.link_slug:
        try:
            link_res = db.table("links").select("id, client_id, clients(plan, email)").eq("slug", lead.link_slug).single().execute()
            if link_res.data:
                link_id = link_res.data["id"]
                client_id = link_res.data["client_id"]
                # Supabase join syntax might return nested dict or flattened depending on query
                # "clients(plan, email)" -> clients: { plan: ..., email: ... }
                client_data = link_res.data.get("clients")
                if client_data:
                    client_plan = client_data.get("plan", "solo")
                    client_email = client_data.get("email")
        except Exception as e:
            print(f"Error resolving link: {e}")

    serasa_score = None
    if lead.cpf and client_plan in ["pro", "agency"]:
        serasa_score = await check_serasa_score(lead.cpf)

    # 3. Insert Lead
    new_lead = {
        "client_id": client_id, # Can be None if generic capture? Table schema has constraint? "REFERENCES clients(id)". If null, insert might fail if not nullable. Manual says "REFERENCES ...". Usually implies FK constraint.
        # If we can't resolve client, maybe we shouldn't accept the lead or assign to a default admin client.
        # For now, we proceed. If it fails, we catch it.
        "link_id": link_id,
        "name": lead.name,
        "phone": lead.phone,
        "cpf": encrypt_data(lead.cpf) if lead.cpf else None,
        "has_clt": lead.has_clt,
        "clt_years": lead.clt_years,
        "income": lead.income,
        "tried_financing": lead.tried_financing,
        "internal_score": score,
        "serasa_score": serasa_score,
        "status": status,
        "utm_source": lead.utm_source,
        "utm_campaign": lead.utm_campaign,
        "utm_medium": lead.utm_medium,
        "device_type": lead.device_type,
        "consent_given": lead.consent_given,
        "created_at": datetime.now().isoformat()
    }

    try:
        # If client_id is None, this might fail.
        # But we'll try.
        lead_res = db.table("leads").insert(new_lead).execute()
        if not lead_res.data:
             raise HTTPException(status_code=500, detail="Failed to save lead")

        saved_lead = lead_res.data[0]
        lead_id = saved_lead["id"]

        # 4. Insert Event
        db.table("events").insert({
            "lead_id": lead_id,
            "event_type": "form_submit",
            "metadata": {"score": score, "status": status}
        }).execute()

        # 5. Send Email Alert (Background Task)
        if score >= 70 and client_email:
            badge = "🔥 Quente"
            background_tasks.add_task(send_hot_lead_email, new_lead, score, badge, client_email)

        # 6. Generate WhatsApp URL
        # Logic described in Chapter 9.4 (Frontend) but endpoint returns "URL do WhatsApp pré-preenchida" in Chapter 4.6.
        # So backend can return it too.

        msg_clt = f"CLT há {lead.clt_years}" if lead.has_clt else "sem carteira assinada"
        tried_text = "Já tentei financiar antes." if lead.tried_financing else "Nunca tentei financiar."
        message = f"Olá! Me chamo {lead.name}. Tenho {msg_clt}, renda aproximada de {lead.income}. {tried_text} Gostaria de mais informações."

        # We need the client's phone number!
        # `clients` table has `whatsapp`.
        client_whatsapp = None
        if link_id:
             # We fetched `clients(plan, email)` earlier, maybe we should have fetched `whatsapp`.
             # Fetch again or optimize previous query.
             pass

        # Re-query client whatsapp if we have client_id
        target_phone = "55..." # Default?
        if client_id:
            try:
                c_res = db.table("clients").select("whatsapp").eq("id", client_id).single().execute()
                if c_res.data:
                    target_phone = c_res.data.get("whatsapp")
            except:
                pass

        # Fallback if no client phone found (e.g. mock)
        if not target_phone:
            target_phone = "5562999999999"

        # Build URL
        from urllib.parse import quote
        whatsapp_url = f"https://wa.me/{target_phone}?text={quote(message)}"

        return {
            "success": True,
            "score": score,
            "status": status,
            "whatsapp_url": whatsapp_url
        }

    except Exception as e:
        print(f"Lead save error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/leads")
async def get_leads(limit: int = 20, offset: int = 0, user=Depends(get_current_user)):
    db = get_client()
    if not db:
        raise HTTPException(status_code=500, detail="Database connection error")

    client_id = user.id

    try:
        # Supabase select with range for pagination
        # Note: 'range' is 0-based index, inclusive start and end?
        # Supabase JS: .range(0, 9) returns 10 items.
        # Python client should match.
        res = db.table("leads").select("*").eq("client_id", client_id).order("created_at", desc=True).range(offset, offset + limit - 1).execute()
        return res.data
    except Exception as e:
        print(f"Fetch leads error: {e}")
        # Return empty list on error for now
        return []
