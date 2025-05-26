from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    with open("lib/db/schema.sql") as file:
        conn.executescript(file.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete.")
