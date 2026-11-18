class Book:
    counter = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
        Book.counter += 1

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


book1 = Book("The fault in our stars", " John Green")
book2 = Book("Alchemist", " Paulo Coelho")

print(book1)
book1.borrow()
book1.return_book()

print("Total books:", Book.counter)
print(repr(book2))