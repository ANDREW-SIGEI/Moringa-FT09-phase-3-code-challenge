from .connection import get_db_connection  # Ensure this import is active and correct

def create_tables():
    """
    Create tables for authors, magazines, and articles in the database.
    Ensures that the tables are created only if they don't already exist.
    """
    try:
        # Use a context manager for the connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # SQL commands for table creation
            create_authors_table = '''
                CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            '''
            create_magazines_table = '''
                CREATE TABLE IF NOT EXISTS magazines (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL
                )
            '''
            create_articles_table = '''
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    author_id INTEGER,
                    magazine_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES authors (id),
                    FOREIGN KEY (magazine_id) REFERENCES magazines (id)
                )
            '''
            
            # Execute SQL commands
            cursor.execute(create_authors_table)
            cursor.execute(create_magazines_table)
            cursor.execute(create_articles_table)
            
            conn.commit()  # Commit changes
            print("Tables created successfully!")
    
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
