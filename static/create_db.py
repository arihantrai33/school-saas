import sqlite3
import os

# database path
db_path = os.path.join("static", "database.db")

print("Creating DB at:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("""
INSERT OR IGNORE INTO users (email, password)
VALUES ('admin@school.com', '123456')
""")

conn.commit()
conn.close()

print("Database & users table ready!")
