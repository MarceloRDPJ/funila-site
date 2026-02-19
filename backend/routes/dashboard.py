from fastapi import APIRouter, Depends, HTTPException
from database import get_client
from routes.auth import get_current_user

router = APIRouter()

@router.get("/metrics")
async def get_metrics(user=Depends(get_current_user)):
    db = get_client()
    if not db:
        raise HTTPException(status_code=500, detail="Database unavailable")

    client_id = user.id

    try:
        # Get Client Links
        links_res = db.table("links").select("id").eq("client_id", client_id).execute()
        link_ids = [l['id'] for l in links_res.data] if links_res.data else []

        # Count Clicks
        clicks_count = 0
        if link_ids:
            c_res = db.table("clicks").select("id", count="exact", head=True).in_("link_id", link_ids).execute()
            clicks_count = c_res.count if c_res.count is not None else 0

        # Count Leads
        l_res = db.table("leads").select("id", count="exact", head=True).eq("client_id", client_id).execute()
        leads_count = l_res.count if l_res.count is not None else 0

        # Count Hot Leads
        h_res = db.table("leads").select("id", count="exact", head=True).eq("client_id", client_id).eq("status", "hot").execute()
        hot_leads = h_res.count if h_res.count is not None else 0

        conversion = 0
        if clicks_count > 0:
            conversion = (leads_count / clicks_count) * 100

        return {
            "clicks": clicks_count,
            "leads": leads_count,
            "hot_leads": hot_leads,
            "conversion": round(conversion, 1)
        }
    except Exception as e:
        print(f"Metrics error: {e}")
        # Return zeros on error to avoid breaking frontend completely
        return {
            "clicks": 0,
            "leads": 0,
            "hot_leads": 0,
            "conversion": 0
        }
