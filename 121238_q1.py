# Book Class 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


#  LibraryMember Class 
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_books(self):
        print(f"\nBooks borrowed by {self.name}:")
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


#  Main Program Logic 
if __name__ == "__main__":
    # Sample data
    book1 = Book("Python Basics", "John Doe")
    book2 = Book("Intro to Flask", "Jane Smith")
    member = LibraryMember("Alice", "001")

    while True:
        print("\nOptions:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter book title to borrow: ")
            if title.lower() == "python basics":
                member.borrow_book(book1)
            elif title.lower() == "intro to flask":
                member.borrow_book(book2)
            else:
                print("Book not found.")

        elif choice == '2':
            title = input("Enter book title to return: ")
            if title.lower() == "python basics":
                member.return_book(book1)
            elif title.lower() == "intro to flask":
                member.return_book(book2)
            else:
                print("Book not found.")

        elif choice == '3':
            member.list_books()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
