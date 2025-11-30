import json
import logging
from pathlib import Path
from .book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def __init__(self, filepath="data/catalog.json"):
        self.filepath = Path(filepath)
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if not self.filepath.exists():
                self.save_data()

            with open(self.filepath, "r") as file:
                data = json.load(file)
                self.books = [Book(**entry) for entry in data]

            logging.info("Catalog loaded successfully.")

        except (json.JSONDecodeError, FileNotFoundError):
            logging.error("Corrupted or missing JSON file. Creating a new one.")
            self.books = []
            self.save_data()

    def save_data(self):
        try:
            with open(self.filepath, "w") as file:
                json.dump([b.to_dict() for b in self.books], file, indent=4)
            logging.info("Catalog saved successfully.")
        except Exception as e:
            logging.error(f"Error saving file: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books
