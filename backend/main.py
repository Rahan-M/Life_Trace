# main.py
from fastapi import FastAPI
from supabase_client import supabase

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/supabase-health")
def supabase_health():
    # simplest possible request
    result = supabase.auth.get_session()
    return {
        "connected": True,
        "result": result
    }

@app.get("/test-read")
def test_read():
    response = supabase.table("users").select("*").limit(5).execute()
    return {
        "data": response.data,
        "count": len(response.data)
    }

@app.post("/test-insert")
def test_insert():
    payload = {
        "name": "Rahan",
        "date_of_birth": "2006-08-28",
        "gender": "M"
    }

    response = supabase.table("users").insert(payload).execute()

    return {
        "inserted": response.data
    }
