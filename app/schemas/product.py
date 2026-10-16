
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict,Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    quantity: int = Field(ge=0)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: Decimal
    quantity: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    quantity: int = Field(ge=0)
