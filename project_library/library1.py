class Library:
    def __init__(self):
        self.book_storage = []

    def add_book(self, new_book):
        self.book_storage.append(new_book)
        new_book.set_availability(True)

    def rm__book(self, book):
        self.book_storage.remove(book)
        book.set_availability(False)

    def get_book_storage(self):
        return self.book_storage

    def get_available_books(self):
        result = []
        for book in self.book_storage:
            if book.get_availability() is True:
                result.append(book)
        return result