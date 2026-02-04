# routes/profile.py

from fastapi import APIRouter, Depends
from auth.deps import get_current_user
from schemas.profile import ProfileUpdate
from db import supabase

router = APIRouter()

@router.post("/profile/complete")
def complete_profile(
    data: ProfileUpdate,
    user_id: str = Depends(get_current_user)
):
    response = (
        supabase
        .table("users")
        .update(data.model_dump())
        .eq("id", user_id)   # ← THIS is how we find the row
        .execute()
    )

    return {"status": "profile updated"}
