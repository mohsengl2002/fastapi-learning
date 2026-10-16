"""
setup_project.py
ساخت خودکار ساختار پروژه FastAPI
اجرا:  python setup_project.py
"""

from pathlib import Path

# ---------- ۱. تعریف ساختار پروژه ----------
# کلید = مسیر فایل/پوشه ، مقدار = محتوای فایل (None = فقط پوشه)
PROJECT_STRUCTURE = {
    # پوشهها (بدون محتوا)
    "app": None,
    "app/routers": None,
    "app/models": None,
    "app/schemas": None,
    "app/core": None,
    "tests": None,

    # فایلهای __init__.py خالی
    "app/__init__.py": "",
    "app/routers/__init__.py": "",
    "app/models/__init__.py": "",
    "app/schemas/__init__.py": "",
    "app/core/__init__.py": "",
    "tests/__init__.py": "",

    # ---------- main.py ----------
    "app/main.py": '''\
from fastapi import FastAPI
from app.routers import users, items

app = FastAPI(
    title="FastAPI Learning",
    description="پروژه یادگیری FastAPI",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


# اتصال روترها
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
''',

    # ---------- routers/users.py ----------
    "app/routers/users.py": '''\
from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

# دیتابیس موقت در حافظه
fake_db: dict[int, dict] = {}
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
''',

    # ---------- routers/items.py ----------
    "app/routers/items.py": '''\
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_items():
    return [{"id": 1, "name": "item-1"}, {"id": 2, "name": "item-2"}]


@router.get("/{item_id}")
def get_item(item_id: int):
    return {"id": item_id, "name": f"item-{item_id}"}
''',

    # ---------- schemas/user.py ----------
    "app/schemas/user.py": '''\
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0, le=120)


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserRead(UserBase):
    id: int
''',

    # ---------- core/config.py ----------
    "app/core/config.py": '''\
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

APP_NAME = "FastAPI Learning"
DEBUG = True
DATABASE_URL = f"sqlite:///{BASE_DIR / 'app.db'}"
''',

    # ---------- tests/test_main.py ----------
    "tests/test_main.py": '''\
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello FastAPI!"}


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
''',

    # ---------- requirements.txt ----------
    "requirements.txt": '''\
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
pydantic[email]>=2.7.0
python-dotenv>=1.0.0
pytest>=8.0.0
httpx>=0.27.0
''',

    # ---------- .gitignore ----------
    ".gitignore": '''\
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
env/
.env
*.db
*.sqlite3
.pytest_cache/
.mypy_cache/
.ruff_cache/
.vscode/
.idea/
dist/
build/
''',

    # ---------- README.md ----------
    "README.md": '''\
# FastAPI Learning

پروژه تمرینی FastAPI

## راهاندازی

```bash
python -m venv .venv
.venv\\Scripts\\Activate.ps1      # ویندوز PowerShell
pip install -r requirements.txt