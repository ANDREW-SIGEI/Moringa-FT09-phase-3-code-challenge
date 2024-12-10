from database.connection import get_db_connection


class Author:
    def __init__(self, name):
        self.name = name
        self._id = None
        self.save()

    @property
    def id(self):
        if self._id is None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM authors WHERE name = ?", (self.name,))
            self._id = cursor.fetchone()[0]
            conn.close()
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after initialization.")
        self._name = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE authors.id = ?
        """, (self.id,))
        articles = [row[0] for row in cursor.fetchall()]
        conn.close()
        return articles
