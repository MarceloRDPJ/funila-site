import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

def get_client() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not url or not key:
        # Fallback for development/testing if env vars are missing or partial
        if os.environ.get("ENVIRONMENT") == "development":
             print("Warning: Supabase credentials missing. Using placeholder.")
             return None
        raise ValueError("Supabase credentials (SUPABASE_URL, SUPABASE_SERVICE_KEY) not found.")
    return create_client(url, key)
