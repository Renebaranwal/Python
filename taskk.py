from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"'{self.title}' by {self.author} - {status}"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = {} 

    def can_borrow(self):
        return len(self.borrowed_books) < 3

    def __str__(self):
        return f"{self.name} | Books Borrowed: {len(self.borrowed_books)}"


class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def register_member(self, name):
        if name not in self.members:
            self.members[name] = Member(name)
        else:
            print(f"{name} is already a registered member.")

    def find_books(self, keyword):
        keyword = keyword.lower()
        return [book for book in self.books if keyword in book.title.lower() or keyword in book.author.lower()]

    def view_available_books(self):
        return [book for book in self.books if book.available]

    def borrow_book(self, member_name, title):
        member = self.members.get(member_name)
        if not member:
            print(f"Member '{member_name}' not found.")
            return

        if not member.can_borrow():
            print("Borrow limit reached (max 3 books).")
            return

        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                member.borrowed_books[book] = datetime.now()
                print(f"{member_name} borrowed '{book.title}'")
                return

        print(f"Book '{title}' is not available.")

    def return_book(self, member_name, title):
        member = self.members.get(member_name)
        if not member:
            print(f"Member '{member_name}' not found.")
            return

        for book in list(member.borrowed_books):
            if book.title.lower() == title.lower():
                borrow_date = member.borrowed_books.pop(book)
                book.available = True
                days = (datetime.now() - borrow_date).days
                fine = max(0, days - 7) * 10
                print(f"{member_name} returned '{book.title}'. Fine: ₹{fine}")
                return

        print(f"'{title}' was not borrowed by {member_name}.")


# ------------------ Execution ------------------

library = Library()
library.add_book("The Alchemist", "Paulo Coelho")
library.add_book("Harry Potter", "J.K. Rowling")
library.add_book("Python Basics", "John Doe")

library.register_member("Alice")
library.register_member("Bob")

library.borrow_book("Alice", "The Alchemist")
library.borrow_book("Alice", "Harry Potter")

print("\nAvailable Books:")
for book in library.view_available_books():
    print(book)

print("\nSearch Results for 'Python':")
for book in library.find_books("Python"):
    print(book)

library.return_book("Alice", "The Alchemist")
