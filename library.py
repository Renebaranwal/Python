from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {'Available' if self.available else 'Borrowed'}"

class Member:
    MAX_BORROW = 3

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}

    def borrow_book(self, book, borrow_date):
        if len(self.borrowed_books) >= Member.MAX_BORROW:
            print(f"{self.name} has already borrowed 3 books.")
            return False
        if not book.available:
            print("Book is currently not available.")
            return False

        self.borrowed_books[book.isbn] = borrow_date
        book.available = False
        print(f"{self.name} borrowed '{book.title}'.")
        return True

    def return_book(self, book, return_date):
        if book.isbn not in self.borrowed_books:
            print(f"{self.name} did not borrow this book.")
            return

        borrow_date = self.borrowed_books.pop(book.isbn)
        book.available = True
        days_borrowed = (return_date - borrow_date).days
        fine = max(0, (days_borrowed - 14) * 2)
        print(f"Book returned. Days borrowed: {days_borrowed}, Fine: ₹{fine}")

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, isbn):
        if isbn in self.books:
            print("Book with this ISBN already exists.")
            return
        self.books[isbn] = Book(title, author, isbn)
        print(f"Book '{title}' added.")

    def register_member(self, name, member_id):
        if member_id in self.members:
            print("Member already registered.")
            return
        self.members[member_id] = Member(name, member_id)
        print(f"Member '{name}' registered.")

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members or isbn not in self.books:
            print("Invalid member ID or book ISBN.")
            return
        member = self.members[member_id]
        book = self.books[isbn]
        member.borrow_book(book, datetime.today())

    def return_book(self, member_id, isbn):
        if member_id not in self.members or isbn not in self.books:
            print("Invalid member ID or book ISBN.")
            return
        member = self.members[member_id]
        book = self.books[isbn]
        member.return_book(book, datetime.today())

    def view_books(self):
        print("Available Books:")
        for book in self.books.values():
            print(book)

    def search_book(self, keyword):
        print(f"Search Results for '{keyword}':")
        found = False
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No matching books found.")

def main():
    lib = Library()
    lib.add_book("Python Programming", "John Zelle", "101")
    lib.add_book("Introduction to AI", "Stuart Russell", "102")
    lib.add_book("Clean Code", "Robert Martin", "103")
    lib.register_member("Alice", "M001")
    lib.register_member("Bob", "M002")
    lib.borrow_book("M001", "101")
    lib.borrow_book("M001", "102")
    lib.borrow_book("M001", "103")
    lib.borrow_book("M001", "102")
    lib.view_books()
    lib.search_book("python")
    lib.search_book("martin")
    lib.return_book("M001", "101")
    lib.view_books()

if __name__ == "__main__":
    main()
