from library_manager.book import Book
from library_manager.inventory import LibraryInventory

def menu():
    print("\n===== LIBRARY INVENTORY MANAGER =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
    print("=====================================")

def main():
    inventory = LibraryInventory()

    while True:
        try:
            menu()
            choice = input("Enter choice: ")

            if choice == "1":
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")

                book = Book(title, author, isbn)
                inventory.add_book(book)
                print("Book added successfully!")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)

                if book and book.issue():
                    inventory.save_data()
                    print("Book issued successfully!")
                else:
                    print("Cannot issue — book unavailable.")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = inventory.search_by_isbn(isbn)

                if book and book.return_book():
                    inventory.save_data()
                    print("Book returned successfully!")
                else:
                    print("Cannot return — wrong ISBN.")

            elif choice == "4":
                books = inventory.display_all()
                if not books:
                    print("No books in catalog.")
                else:
                    for b in books:
                        print(b)

            elif choice == "5":
                key = input("Enter title to search: ")
                results = inventory.search_by_title(key)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("No matching books found.")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid input.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

