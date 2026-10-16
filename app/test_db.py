from sqlalchemy import text
from app.database.connection import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION()"))
        print("Connected to MySQL")
        print("MySQL version:", result.scalar())
except Exception as error:
    print("Database connection failed")
    print(error)