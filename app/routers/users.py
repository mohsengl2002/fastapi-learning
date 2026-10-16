from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

fake_db = {}
_next_id = 1


@router.get("/", response_model=list[UserRead])
def list_users():
    return list(fake_db.values())


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_db[user_id]


@router.post("/", response_model=UserRead, status_code=201)
def create_user(payload: UserCreate):
    global _next_id
    user = {"id": _next_id, **payload.model_dump()}
    fake_db[_next_id] = user
    _next_id += 1
    return user
