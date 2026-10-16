from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

APP_NAME = "FastAPI Learning"
DEBUG = True
DATABASE_URL = f"sqlite:///{BASE_DIR / 'app.db'}"
