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


def main():
	print("MIT ADT University, Pune")
	print("Library Management System")
	print("=" * 32)

	library = Library()

	book1 = Book("Python Programming", "John Zelle", "9781590282755")
	book2 = Book("Data Structures", "Narasimha Karumanchi", "9788193245278")
	book3 = Book("Clean Code", "Robert C. Martin", "9780132350884")

	patron1 = Patron("Aarav Sharma", "P001")
	patron2 = Patron("Neha Patil", "P002")

	print("\nAdding books...")
	for book in (book1, book2, book3):
		print(f"Added: {book.title}" if library.add_book(book) else f"Book already exists: {book.title}")

	print("\nRegistering patrons...")
	for patron in (patron1, patron2):
		print(f"Registered: {patron.name}" if library.register_patron(patron) else f"Patron already exists: {patron.name}")

	success, message = library.borrow_book("P001", "9781590282755")
	print("\n" + message)

	success, message = library.borrow_book("P002", "9780132350884")
	print(message)

	success, message = library.return_book("P001", "9781590282755")
	print("\n" + message)

	success, message = library.borrow_book("P002", "9781590282755")
	print(message)

	library.display_books()
	library.display_patrons()


if __name__ == "__main__":
	main()
