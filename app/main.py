
from fastapi import FastAPI
from app.routes.products import router as products_router

app = FastAPI(title="FastAPI MySQL Project")

app.include_router(products_router)
