class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def get_category(self):
        if self.price >= 500:
            return "Premium"
        return "Standard"

    def __str__(self):
        return (
            f"Book ID: {self.book_id}, "
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Price: ₹{self.price}, "
            f"Category: {self.get_category()}"
        )


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"\nBooks in {self.name}:\n")
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)


def main():
    library = Library("City Central Library")

    library.add_book(Book(101, "Python Crash Course", "Eric Matthes", 650))
    library.add_book(Book(102, "Clean Code", "Robert C. Martin", 420))
    library.add_book(Book(103, "Data Structures", "Seymour Lipschutz", 780))
    library.add_book(Book(104, "DBMS Basics", "Navathe", 350))

    library.display_books()


if __name__ == "__main__":
    main()
