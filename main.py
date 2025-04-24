import json


class BookCollection: # class works as a printer
    """A class to Manage a collection of books, allowing users to store and organize their reading materials"""
    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage"""
        self.book_list = []
        self.storage_file = 'books_data.json'
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file does'nt exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file,"r") as file:
                self.book_list = json.load(file)
        except ( FileNotFoundError, json.JSONDecodeError):
            self.book_list = []
    
    def save_to_file(self):
        """Save the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)


    def create_new_book(self):
        """Add a new Book to the collection by gathering information from the user."""
        book_title = input("Enter the book's title: ")
        book_author = input("Enter the author's name: ")
        publication_year = int(input("Enter the publication year: "))
        book_genre = input("Enter the genre of the book: ")
        is_book_read = input("Have you read the book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print(f"Added {book_title} to the collection!\n")

    def delete_book(self):
        """Delete a book from the collection by its title."""
        book_title = input("Enter the title of the book you want to delete: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print(f"Deleted {book_title} from the collection!\n")
                return
            print("Book not found in the collection.\n")
    
    def find_book(self):
        """Search for a book by its title or Author name."""
        search_type = input("Search by :\n1. Title\n2. Author\nEnter your choice by number (1/2): ")
        search_text = input("Enter the search terms: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()

        ]
        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index }. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status} ") 
        else:
            print("No books found matching the search terms.\n")


    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to update: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"Enter new title for {book_title}: ") or book["title"]
                book["author"] = input(f"Enter new author for {book_title}: ") or book["author"]
                book["year"] = int(input(f"Enter new publication year for {book_title}: ") or book["year"])
                book["genre"] = input(f"Enter new genre for {book_title}: ") or book["genre"]
                book["read"] = input(f"Have you read {book_title}? (yes/no): ").strip().lower() == "yes"
                self.save_to_file()
                print(f"Updated {book_title} in the collection!\n")
                return
        print("Book not found in the collection.\n")


    def display_books(self):
        """Display all the books in the collection."""
        if not self.book_list:
            print("Your Books Collection is empty")
            return
        
        print("Your Books Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        print()


    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)
        read_books = sum(1 for book in self.book_list if book["read"])
        completed_percentage = ((read_books / total_books * 100)  if total_books > 0 else 0 )      
        print(f"Total Books in Collection: {total_books}")   
        print(f"Books Read: {completed_percentage:.2f}%\n") 

    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.display_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()       

     

        
              
       
      
    