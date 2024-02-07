class User:
    # добавил айди
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.books = []

    def __str__(self):
        return f'{self.name} id: {self.id}'


    def take_book(self, book):
        self.books.append(book)
        book.set_availability(False)

    def return_book(self, book):
        self.books.remove(book)
        book.set_availability(True)

    def get_book(self):
        return self.books