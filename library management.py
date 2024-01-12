class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"Book borrowed successfully: {self.title}")
        else:
            print("Sorry, the book is not available.")

    def return_book(self):
        self.is_available = True
        print(f"Book returned successfully: {self.title}")


class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


class Member:
    def _init_(self, name):
        self.name = name


if _name_ == "_main_":
    book1 = Book("The Catcher in the Rye", "J.D. Salinger")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)

    member = Member("John Doe")

    library.display_available_books()

    borrowed_book = library.find_book("To Kill a Mockingbird")
    if borrowed_book:
        borrowed_book.borrow_book()

    library.display_available_books()

    borrowed_book = library.find_book("To Kill a Mockingbird")
    if borrowed_book:
        borrowed_book.return_book()
