from database.connection import get_db_connection

def test_connection():
    try:
        conn = get_db_connection()
        print("Connection successful!")
        print("SQLite Version:", conn.execute("SELECT sqlite_version();").fetchone()[0])
        conn.close()
        print("Connection closed successfully.")
    except Exception as e:
        print("Failed to connect:", e)

if __name__ == "__main__":
    test_connection()
