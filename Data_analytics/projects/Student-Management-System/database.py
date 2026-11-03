
import sqlite3
# Database file name
DB_NAME = "students.db"

# Establish database connection
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
# Create students table if it does not exist
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            course TEXT NOT NULL,
            city TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("Database and students table created successfully!")
