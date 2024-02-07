from books import Book
from library1 import Library


def get_library_with_books():
    library = Library()

    book1 = Book('Гарри Поттер', 'Дж. Роулинг', "Фентези")
    book2 = Book('1984', 'Дж. Оруэлл', 'Роман-антиутопия')
    book3 = Book('Гении и аутсайдеры ', 'М. Гледуелл', 'Психология')
    book4 = Book('Дневник памяти', 'Николас Спаркс', 'Роман')
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    return library