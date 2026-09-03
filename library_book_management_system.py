"""Library Book Management System and Climbing Stairs dynamic programming."""


class Book:
    """Store book details and determine its price category."""

    def __init__(self, title, author_name, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.title = title
        self.author_name = author_name
        self.price = price

    def get_category(self):
        if self.price >= 1000:
            return "Premium"
        if self.price >= 500:
            return "Standard"
        return "Basic"

    def display_information(self):
        """Display complete book information."""
        print(
            f"Title: {self.title}, Author: {self.author_name}, "
            f"Price: Rs. {self.price:.2f}, Category: {self.get_category()}"
        )

    def __str__(self):
        return (
            f"{self.title} by {self.author_name} | "
            f"Rs. {self.price:.2f} | {self.get_category()}"
        )


class Library:
    """Maintain a collection of books."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added.")
        self.books.append(book)

    def display_books(self):
        """Display all books in the library."""
        print("\nLibrary Book Collection")
        print("=" * 30)
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            print(f"- {book}")


def climbing_stairs(stairs):
    """Return ways to climb stairs using one or two steps at a time."""
    if stairs < 0:
        raise ValueError("Number of stairs cannot be negative.")
    if stairs <= 1:
        return 1

    ways = [0] * (stairs + 1)
    ways[0] = 1
    ways[1] = 1

    for step in range(2, stairs + 1):
        ways[step] = ways[step - 1] + ways[step - 2]

    return ways[stairs]


def main():
    library = Library()
    library.add_book(Book("Python Crash Course", "Eric Matthes", 650))
    library.add_book(Book("Clean Code", "Robert C. Martin", 420))
    library.add_book(Book("Data Structures", "Seymour Lipschutz", 1200))

    library.display_books()
    print(f"\nWays to climb 5 stairs: {climbing_stairs(5)}")


if __name__ == "__main__":
    main()
