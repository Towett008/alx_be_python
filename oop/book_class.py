class Book:
    def __init__(self, title, author, year):
        #constuctor that initializes the book attributes
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        # Destuctor that prints a message when the object is deleted
        print(f"Deleting {self.title}")
    def __str__(self):
        #Returns a user-friendly string represantation of the book
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        #Returns an official represantation that can recreate the object.
        return f"Book('{self.title}', '{self.author}', {self.year})"
       
        