class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}')"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author} ({self.file_size} KB)"

    def __repr__(self) -> str:
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author} - {self.page_count} pages"

    def __repr__(self) -> str:
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book (or subclass) instance")
        self.books.append(book)

    def list_books(self) -> None:
        if not self.books:
            print("Library is empty.")
        else:
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")
   
