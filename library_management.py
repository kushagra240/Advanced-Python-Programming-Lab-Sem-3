class Book:
	def __init__(self, title, author, isbn):
		self.title = title
		self.author = author
		self.isbn = isbn
		self.is_borrowed = False

	def borrow(self):
		if self.is_borrowed:
			return False
		self.is_borrowed = True
		return True

	def return_book(self):
		if not self.is_borrowed:
			return False
		self.is_borrowed = False
		return True

	def __str__(self):
		status = "Borrowed" if self.is_borrowed else "Available"
		return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"


class Patron:
	def __init__(self, name, patron_id):
		self.name = name
		self.patron_id = patron_id
		self.borrowed_books = []

	def borrow_book(self, book):
		if book in self.borrowed_books:
			return False
		self.borrowed_books.append(book)
		return True

	def return_book(self, book):
		if book not in self.borrowed_books:
			return False
		self.borrowed_books.remove(book)
		return True

	def __str__(self):
		borrowed = ", ".join(book.title for book in self.borrowed_books) or "No books borrowed"
		return f"{self.name} (ID: {self.patron_id}) -> {borrowed}"


class Library:
	def __init__(self):
		self.books = {}
		self.patrons = {}

	def add_book(self, book):
		if book.isbn in self.books:
			return False
		self.books[book.isbn] = book
		return True

	def register_patron(self, patron):
		if patron.patron_id in self.patrons:
			return False
		self.patrons[patron.patron_id] = patron
		return True

	def borrow_book(self, patron_id, isbn):
		patron = self.patrons.get(patron_id)
		book = self.books.get(isbn)

		if patron is None or book is None:
			return False, "Patron or book not found."

		if not book.borrow():
			return False, f"'{book.title}' is already borrowed."

		patron.borrow_book(book)
		return True, f"{patron.name} borrowed '{book.title}'."

	def return_book(self, patron_id, isbn):
		patron = self.patrons.get(patron_id)
		book = self.books.get(isbn)

		if patron is None or book is None:
			return False, "Patron or book not found."

		if not patron.return_book(book):
			return False, f"{patron.name} did not borrow '{book.title}'."

		book.return_book()
		return True, f"{patron.name} returned '{book.title}'."

	def display_books(self):
		print("\nBooks in Library:")
		if not self.books:
			print("No books available.")
			return
		for book in self.books.values():
			print(f"- {book}")

	def display_patrons(self):
		print("\nRegistered Patrons:")
		if not self.patrons:
			print("No patrons registered.")
			return
		for patron in self.patrons.values():
			print(f"- {patron}")


def add_sample_data(library):
	library.add_book(Book("Python Basics", "John Smith", "101"))
	library.add_book(Book("Data Science", "Asha Mehta", "102"))
	library.add_book(Book("Clean Code", "Robert Martin", "103"))
	library.register_patron(Patron("Sam", "P1"))
	library.register_patron(Patron("Riya", "P2"))


def menu():
	print("\nMenu")
	print("1. Add book")
	print("2. Register patron")
	print("3. Borrow book")
	print("4. Return book")
	print("5. Show books")
	print("6. Show patrons")
	print("7. Exit")


def main():
	print("MIT ADT University, Pune")
	print("Library Management System")
	print("=" * 32)

	library = Library()

	add_sample_data(library)
	print("\nSample data added for quick use.")

	while True:
		menu()
		choice = input("Enter your choice: ").strip()

		if choice == "1":
			title = input("Enter book title: ").strip()
			author = input("Enter author name: ").strip()
			isbn = input("Enter ISBN: ").strip()
			book = Book(title, author, isbn)
			print("Book added." if library.add_book(book) else "Book already exists.")

		elif choice == "2":
			name = input("Enter patron name: ").strip()
			patron_id = input("Enter patron ID: ").strip()
			patron = Patron(name, patron_id)
			print("Patron registered." if library.register_patron(patron) else "Patron already exists.")

		elif choice == "3":
			patron_id = input("Enter patron ID: ").strip()
			isbn = input("Enter ISBN: ").strip()
			success, message = library.borrow_book(patron_id, isbn)
			print(message)

		elif choice == "4":
			patron_id = input("Enter patron ID: ").strip()
			isbn = input("Enter ISBN: ").strip()
			success, message = library.return_book(patron_id, isbn)
			print(message)

		elif choice == "5":
			library.display_books()

		elif choice == "6":
			library.display_patrons()

		elif choice == "7":
			print("Exiting program.")
			break

		else:
			print("Invalid choice. Please try again.")


if __name__ == "__main__":
	main()
