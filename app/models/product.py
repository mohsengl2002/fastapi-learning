
from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from app.database.connection import Base


class ProductDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    created_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default="CURRENT_TIMESTAMP",
    )
