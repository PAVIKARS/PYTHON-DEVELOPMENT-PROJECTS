class Book:
    """A class representing a book"""

    def __init__(self, title, author, publication_year, ISBN, quantity):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN = ISBN
        self.quantity = quantity

class Library:
    """A class representing a library"""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)

    def remove_book(self, book):
        """Remove a book from the library"""
        self.books.remove(book)

    def search_book_by_title(self, title):
        """Search for a book by title"""
        for book in self.books:
            if book.title == title:
                return book
        return None

    def search_book_by_author(self, author):
        """Search for a book by author"""
        matching_books = []
        for book in self.books:
            if book.author == author:
                matching_books.append(book)
        return matching_books

    def search_book_by_ISBN(self, ISBN):
        """Search for a book by ISBN"""
        for book in self.books:
            if book.ISBN == ISBN:
                return book
        return None

    def lend_book(self, book):
        """Lend a book to a borrower"""
        if book.quantity == 0:
            raise ValueError("Book is not available")
        book.quantity -= 1

    def return_book(self, book):
        """Return a book to the library"""
        book.quantity += 1

# Example usage: create a library and add some books
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-0-7432-7356-5", 2)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "978-0-446-31078-9", 1)
book3 = Book("1984", "George Orwell", 1949, "978-0-141-19136-2", 3)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for a book by title
search_title = "1984"
book = library.search_book_by_title(search_title)
if book:
    print("Found book:", book.title)
else:
    print("Book not found")

# Search for books by author
search_author = "Harper Lee"
matching_books = library.search_book_by_author(search_author)
if len(matching_books) > 0:
    print("Found", len(matching_books), "books by", search_author)
    for book in matching_books:
        print(book.title)
else:
    print("No books found by", search_author)

# Lend a book
borrowed_book = book1
try:
    library.lend_book(borrowed_book)
    print("Book", borrowed_book.title, "has been borrowed")
except ValueError as e:
    print("Error:", e)

# Return a book
returned_book = book1
library.return_book(returned_book)
print("Book", returned_book.title, "has been returned")
