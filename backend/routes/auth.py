import os
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verifies the JWT token with Supabase Auth.
    Returns the user object if valid.
    """
    token = credentials.credentials
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_ANON_KEY")

    if not url or not key:
        # Development bypass if no env
        if os.environ.get("ENVIRONMENT") == "development":
            return {"id": "dev-user-id", "email": "dev@example.com"}

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Supabase configuration missing"
        )

    supabase: Client = create_client(url, key)

    try:
        # Verify token by calling getUser (which validates the session)
        user_response = supabase.auth.get_user(token)
        if not user_response or not user_response.user:
             raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_response.user
    except Exception as e:
        # print(f"Auth error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.get("/me")
async def read_users_me(user = Depends(get_current_user)):
    return user
