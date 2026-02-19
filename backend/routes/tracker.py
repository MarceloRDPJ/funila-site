import hashlib
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from database import get_client
from ua_parser import user_agent_parser

router = APIRouter()

@router.get("/t/{slug}")
async def track_and_redirect(slug: str, request: Request):
    db = get_client()
    if not db:
        raise HTTPException(status_code=500, detail="Database connection error")

    try:
        link_response = db.table("links").select("*").eq("slug", slug).single().execute()
        if not link_response.data:
            raise HTTPException(status_code=404)
        link_data = link_response.data
    except Exception as e:
        # print(f"Link not found or DB error: {e}")
        raise HTTPException(status_code=404)

    # Anonimiza o IP (LGPD compliance)
    ip = request.client.host or ""
    ip_hash = hashlib.sha256(ip.encode()).hexdigest()

    # Parse do User-Agent
    ua_str = request.headers.get("user-agent", "")
    ua = user_agent_parser.Parse(ua_str)

    device_family = ua.get("device", {}).get("family", "")
    device = "mobile" if device_family in ["iPhone", "Android", "Generic Smartphone"] else "desktop"

    os_family = ua.get("os", {}).get("family", "Unknown")

    referrer = request.headers.get("referer", "")

    # Salva o clique (não bloqueia o redirect ideally, but synchronous here)
    try:
        db.table("clicks").insert({
            "link_id": link_data["id"],
            "ip_hash": ip_hash,
            "device_type": device,
            "os": os_family,
            "referrer": referrer,
        }).execute()
    except Exception as e:
        print(f"Failed to log click: {e}")

    return RedirectResponse(url=link_data["destination"], status_code=302)
