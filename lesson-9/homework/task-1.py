import json

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["is_borrowed"])

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    def __init__(self, name, borrowed_books=None):
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum of 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        self.borrowed_books.append(book.title)
        book.is_borrowed = True

    def return_book(self, book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
            book.is_borrowed = False

    def to_dict(self):
        return {
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Member(data["name"], data["borrowed_books"])

    def __str__(self):
        borrowed_titles = ', '.join(self.borrowed_books) or 'None'
        return f"{self.name} (Borrowed books: {borrowed_titles})"

class Library:
    def __init__(self, books_file="books.json", members_file="members.json"):
        self.books_file = books_file
        self.members_file = members_file
        self.books = self.load_books()
        self.members = self.load_members()

    def save_books(self):
        with open(self.books_file, "w") as file:
            json.dump([book.to_dict() for book in self.books], file)

    def load_books(self):
        try:
            with open(self.books_file, "r") as file:
                return [Book.from_dict(data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_members(self):
        with open(self.members_file, "w") as file:
            json.dump([member.to_dict() for member in self.members], file)

    def load_members(self):
        try:
            with open(self.members_file, "r") as file:
                return [Member.from_dict(data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        self.save_books()

    def add_member(self, name):
        self.members.append(Member(name))
        self.save_members()

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"The book '{title}' does not exist in the library.")

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)
        self.save_books()
        self.save_members()

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)
        self.save_books()
        self.save_members()

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise ValueError(f"Member '{name}' not found.")

    def __str__(self):
        books_str = '\n'.join(str(book) for book in self.books)
        members_str = '\n'.join(str(member) for member in self.members)
        return f"Library Books:\n{books_str}\n\nLibrary Members:\n{members_str}"

if __name__ == "__main__":
    library = Library()

    while True:
        print("\nChoose an action: [1] Borrow Book [2] Return Book [3] Show Library [4] Add book [5] Add member [6] Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            member_name = input("Enter member name: ").strip()
            book_title = input("Enter book title: ").strip()
            try:
                library.borrow_book(member_name, book_title)
                print(f"{member_name} successfully borrowed '{book_title}'.")
            except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
                print(e)
        elif choice == '2':
            member_name = input("Enter member name: ").strip()
            book_title = input("Enter book title: ").strip()
            try:
                library.return_book(member_name, book_title)
                print(f"{member_name} successfully returned '{book_title}'.")
            except (BookNotFoundException, ValueError) as e:
                print(e)
        elif choice == '3':
            print(library)
        elif choice == '4':
            book_input = input("Enter book (title, author): ").strip()
            try:
                title, author = map(str.strip, book_input.split(","))
                library.add_book(title, author)
                print(f"Book '{title}' by {author} added successfully.")
            except ValueError:
                print("Invalid input format. Please enter in 'title, author' format.")
        elif choice == '5':
            member_name = input("Enter member name: ").strip()
            library.add_member(member_name)
            print(f"Member '{member_name}' added successfully.")
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")