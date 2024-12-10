import sqlite3
import os

# Set the default database location and allow override via environment variable
DATABASE_NAME = os.getenv("DATABASE_NAME", './database/magazine.db')

def get_db_connection():
    """
    Establish a connection to the SQLite database.
    
    Returns:
        sqlite3.Connection: A connection object to interact with the database.
    
    Raises:
        sqlite3.Error: If there's an issue connecting to the database.
    """
    try:
        # Establish connection to the database
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row  # Enables dictionary-like row access for query results
        return conn
    except sqlite3.Error as e:
        # Print error message and raise the exception
        print(f"Error connecting to the database: {e}")
        raise
