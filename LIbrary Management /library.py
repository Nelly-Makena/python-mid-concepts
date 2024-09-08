class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        print(f"Here are the book details: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {availability}")
    def borrow(self):
        if self.available:
            print(f"You have borrowed {self.title}")
            self.available=False
        else:
            print(f"The book {self.title} is not available ")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned the {self.title} book that you borrowed, Thank You !!!!")
        else:
            print(f"The {self.title} book wasn't borrowed ")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"You have added {new_book} to the book list ...")


    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"You have successfully removed the {book.isbn}  isbn from the list ")
            else:
                print(f"The isbn {book.isbn} is not in the book list")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print(f"Here is the book, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
                return book
        print(f"The book with ISBN {isbn} is not in the book list")
        return None
    def display_books(self):
        if not self.books:
            print("Print there are no books at the moment, ")
        else:
            for book in self.books:
                book.display_info()


# Creating a book object with 3 parameters
book_1 = Book("The Cow", "Nelly", "F12345")
book_1.display_info()
book_1.borrow()
book_1.return_book()

Library = Library()
Library.add_book("nelly","nelly","nelly")
Library.display_books()
Library.find_book("nelly")
Library.remove_book("nelly")




