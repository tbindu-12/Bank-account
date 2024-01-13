class Book:
    def _init_(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

    def _str_(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.is_available}"


class Library:
    def _init_(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        for book in self.books:
            print(book)

    def display_members(self):
        for member in self.members:
            print(member)


class Member:
    def _init_(self, member_id, name, is_subscribed=False):
        self.member_id = member_id
        self.name = name
        self.is_subscribed = is_subscribed

    def _str_(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Subscribed: {self.is_subscribed}"

    def borrow_book(self, book):
        if book.is_available:
            print(f"{self.name} borrowed {book.title}.")
            book.is_available = False
        else:
            print(f"Sorry, {book.title} is not available for borrowing.")

    def return_book(self, book):
        print(f"{self.name} returned {book.title}.")
        book.is_available = True


# Example Usage
if _name_ == "_main_":
    book1 = Book(1, "A", "author1")
    book2 = Book(2, "B", "author2")
    book3 = Book(3, "C", "author3")
    member1 = Member(101, "ABC", True)
    member2 = Member(102, "XYZ", False)
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_member(member1)
    library.add_member(member2)

    print("Books in Library:")
    library.display_books()

    print("\nMembers in Library:")
    library.display_members()

    member1.borrow_book(book1)
    member2.borrow_book(book2)

    member1.return_book(book1)
    member2.return_book(book2)

    # Displaying Books after transactions
    print("\nBooks in Library after transactions:")
    library.display_books()
