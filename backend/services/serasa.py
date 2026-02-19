import os
import httpx
from dotenv import load_dotenv

load_dotenv()

async def check_serasa_score(cpf: str) -> int | None:
    token = os.environ.get("SOAWS_TOKEN")
    if not token:
        # If no token, return None (skips check)
        return None

    if not cpf:
        return None

    # Determine endpoint - using a plausible one since manual didn't specify exact path
    url = "https://api.soawebservices.com.br/api/v1/credit/score"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            # Assuming GET or POST with CPF
            response = await client.get(f"{url}?cpf={cpf}", headers=headers, timeout=10.0)

            if response.status_code == 200:
                data = response.json()
                # Assuming the response format has "score"
                return data.get("score")
            else:
                print(f"Serasa API error: {response.status_code} - {response.text}")
                return None
    except Exception as e:
        print(f"Serasa check failed: {e}")
        return None
