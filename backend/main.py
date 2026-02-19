from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import tracker, leads, dashboard, auth
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Funila API", version="1.0.0")

origins = os.getenv("CORS_ORIGINS", "").split(",")
# Ensure at least localhost and app domain are allowed
if not origins or origins == ['']:
    origins = ["https://app.funila.com.br", "http://localhost:3000", "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tracker.router)
app.include_router(leads.router)
app.include_router(dashboard.router)
app.include_router(auth.router, prefix="/auth")

@app.get("/health")
async def health():
    return {"status": "ok"}
