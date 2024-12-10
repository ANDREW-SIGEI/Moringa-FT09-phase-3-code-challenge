from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to collect user input, interact with the database,
    and display stored records.
    """
    # Initialize the database and create tables
    create_tables()

    try:
        # Collect user input with validation
        author_name = input("Enter author's name: ").strip()
        while not author_name:
            author_name = input("Author's name cannot be empty. Enter author's name: ").strip()

        magazine_name = input("Enter magazine name: ").strip()
        while not magazine_name:
            magazine_name = input("Magazine name cannot be empty. Enter magazine name: ").strip()

        magazine_category = input("Enter magazine category: ").strip()
        while not magazine_category:
            magazine_category = input("Magazine category cannot be empty. Enter magazine category: ").strip()

        article_title = input("Enter article title: ").strip()
        while not article_title:
            article_title = input("Article title cannot be empty. Enter article title: ").strip()

        article_content = input("Enter article content: ").strip()
        while not article_content:
            article_content = input("Article content cannot be empty. Enter article content: ").strip()

        # Confirm user wants to save the data
        confirm = input("Do you want to save the data? (yes/no): ").strip().lower()
        if confirm != 'yes':
            logging.info("Data not saved. Exiting.")
            return

        # Connect to the database
        with get_db_connection() as conn:
            cursor = conn.cursor()

            # Create an author
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
            author_id = cursor.lastrowid  # Fetch ID of the new author

            # Create a magazine
            cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', 
                           (magazine_name, magazine_category))
            magazine_id = cursor.lastrowid  # Fetch ID of the new magazine

            # Create an article
            cursor.execute(
                'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                (article_title, article_content, author_id, magazine_id)
            )
            conn.commit()

            logging.info("Data successfully saved!")

            # Fetch all records
            cursor.execute('SELECT * FROM magazines')
            magazines = cursor.fetchall()

            cursor.execute('SELECT * FROM authors')
            authors = cursor.fetchall()

            cursor.execute('SELECT * FROM articles')
            articles = cursor.fetchall()

        # Display results
        print("\nMagazines:")
        if not magazines:
            print("No magazines found.")
        else:
            for magazine in magazines:
                print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

        print("\nAuthors:")
        if not authors:
            print("No authors found.")
        else:
            for author in authors:
                print(Author(author["id"], author["name"]))

        print("\nArticles:")
        if not articles:
            print("No articles found.")
        else:
            for article in articles:
                print(Article(article["id"], article["title"], article["content"], 
                              article["author_id"], article["magazine_id"]))

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
