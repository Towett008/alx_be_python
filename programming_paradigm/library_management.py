class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False #Private attribute
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"'{self.title}' is already checked out.")
    def return_book(self):
        if  self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"'{self.title}' was not checjed out.")
    def is_available(self):
        return not self._is_checked_out
class Library:
    def __init__(self):
        self._books = [] # Private list of Book objects
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
       for book in self._books:
           if book.title == title:
               if book.is_available():
                   book.check_out()
                   print(f"'{title}'  has been  checked out.")
                   return
               else:
                   print(f"'{title}' is already checked out.")
                   return
           print(f"No book with title '{title}' found in the library.")
    def return_book(self, title):
       for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
            print(f"No book with title '{title}' found in the library.")
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
                   
           

      