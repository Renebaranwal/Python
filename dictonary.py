books = {}
members = {}

def add_book(title, count=1):
    if title in books:
        books[title]['total'] += count
        books[title]['available'] += count
    else:
        books[title] = {'total': count, 'available': count}
    print(f"Added {count} copies of '{title}'.")

def borrow_book(member, title):
    if title not in books:
        print(f"Book '{title}' not found.")
        return
    if books[title]['available'] <= 0:
        print(f"No copies of '{title}' are currently available.")
        return
    books[title]['available'] -= 1
    members.setdefault(member, []).append(title)
    print(f"{member} borrowed '{title}'.")

def return_book(member, title):
    if member not in members or title not in members[member]:
        print(f"{member} did not borrow '{title}'.")
        return
    books[title]['available'] += 1
    members[member].remove(title)
    print(f"{member} returned '{title}'.")

def check_borrowed_books(member):
    if member not in members or not members[member]:
        print(f"{member} has not borrowed any books.")
    else:
        print(f"{member} has borrowed: {', '.join(members[member])}")

def display_books():
    print("\nLibrary Catalog:")
    for title, data in books.items():
        print(f"- {title}: Total = {data['total']}, Available = {data['available']}")

def display_members():
    print("\nMembers and Borrowed Books:")
    for member, borrowed in members.items():
        print(f"- {member}: {', '.join(borrowed) if borrowed else 'No books borrowed'}")

def menu():
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Check Member's Borrowed Books")
        print("5. Show All Books")
        print("6. Show All Members")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter book title: ")
            count = int(input("Enter number of copies: "))
            add_book(title, count)
        elif choice == "2":
            member = input("Enter member name: ")
            title = input("Enter book title to borrow: ")
            borrow_book(member, title)
        elif choice == "3":
            member = input("Enter member name: ")
            title = input("Enter book title to return: ")
            return_book(member, title)
        elif choice == "4":
            member = input("Enter member name: ")
            check_borrowed_books(member)
        elif choice == "5":
            display_books()
        elif choice == "6":
            display_members()
        elif choice == "7":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
