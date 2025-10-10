class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title =  title
        self.author = author
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f"Book({self.title!r}, {self.author})"
class Ebook(Book):
    #Derived class representing an ebook with a file size(int ,e.g KB).
    def __init__(self, title: str, author: str, file_size:int) -> None:
        super().__init__(title, author)
        self.file_size = file_size
    def __str__ (self) -> str:
        return f"Ebook: {self.title} by self.author ({self.file_size: } KB)"
    def __repr__(self) ->str:
        return f"Ebook({self.title!r}, {self.author!r}, {self.file_size})"
class PrintBook(Book):
    #Derived class representing a print book with a page  count
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author) 
        self.page_count = page_count
    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author} - {self.page_count} pages"
    def __rep__(self) -> str:
        return f"PrintBook({self.title!r}, {self.author!r}, {self.page_count})"

class Library:
    # Composition example: manages a collection (list) of Book instances.
    def __init__(self) -> None:
        self.books: list[Book] = []
    def add_book (self, book: Book) -> None:
        #Add book/subclass instance to the library
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book (or sublass) instance")
        self.book.append(book)
    def list_books(self) -> None:
        #Print details of each book in the library.
        if not self.books:
            print("Library is empty.")
            return
        for index, book in enumerate (self.books, start=1):
            print(f"{index}.{book}")    