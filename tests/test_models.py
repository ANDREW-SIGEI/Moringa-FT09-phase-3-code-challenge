import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.connection import get_connection

class TestModels(unittest.TestCase):

    def setUp(self):
        """Set up a fresh database before each test."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()
        conn.close()

    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertIsInstance(author.id, int)

    def test_article_creation(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article(author, magazine, "Future of AI")

        self.assertEqual(article.title, "Future of AI")
        self.assertEqual(article.author.id, author.id)
        self.assertEqual(article.magazine.id, magazine.id)

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertIsInstance(magazine.id, int)

    def test_author_articles(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        Article(author, magazine, "Future of AI")
        Article(author, magazine, "AI and Ethics")

        self.assertEqual(len(author.articles()), 2)
        self.assertIn("Future of AI", author.articles())
        self.assertIn("AI and Ethics", author.articles())

    def test_magazine_articles(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        Article(author, magazine, "Future of AI")
        Article(author, magazine, "AI and Ethics")

        self.assertEqual(len(magazine.articles()), 2)
        self.assertIn("Future of AI", magazine.article_titles())
        self.assertIn("AI and Ethics", magazine.article_titles())

    def test_magazine_contributors(self):
        author1 = Author("John Doe")
        author2 = Author("Jane Smith")
        magazine = Magazine("Tech Weekly", "Technology")
        Article(author1, magazine, "Future of AI")
        Article(author2, magazine, "AI and Ethics")

        self.assertEqual(len(magazine.contributors()), 2)
        self.assertIn(author1, magazine.contributors())
        self.assertIn(author2, magazine.contributors())

    def tearDown(self):
        """Clean up database after each test."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        conn.commit()
        conn.close()

if __name__ == "__main__":
    unittest.main()
