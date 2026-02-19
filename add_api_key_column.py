
from db import engine
from sqlalchemy import text

def add_column():
    with engine.connect() as conn:
        conn.execute(text('ALTER TABLE users ADD COLUMN api_key VARCHAR'))
        conn.commit()
    print("Column added successfully")

if __name__ == "__main__":
    add_column()
