from pri import get_library_with_books
from users import User

library = get_library_with_books()

nurzhan = User('Нуржан', 1)
ulan = User('Улан', 2)

print(f"Добро пожаловать в нашу Библиотеку!\n")


valid_user = False
# сделал выход по айди
while not valid_user:
    user_id_input = input("Введите свой id:")

    if user_id_input == '1':
        print(f'Добро пожаловать {nurzhan}')
        valid_user = True
    elif user_id_input == '2':
        print(f'Добро пожаловать {ulan}')
        valid_user = True
    else:
        print('Некорректный id!, Пожалуйста, введите корректный id. ')

    user_input = None

while user_input != 'q':
    print("Меню:\n"
          "1. Все доступные книги\n"
          "2. Взять книгу\n"
          "3. Возврат книги\n"
          "4. Просмотр взятых книг\n"
          "5. Вернуть книгу\n")

    user_input = input("Выберите из меню [1-5] ('q' - выйти): ")

    if user_input == '1':
        print(library.get_available_books())
    elif user_input == '2':
        books = library.get_available_books()
        for i in range(len(books)):
            print(f"{i}. {books[i]}")
        ind = int(input("Выберите книгу: "))

        nurzhan.take_book(books[ind])
        print(f'Пользователь {nurzhan} выбрал книгу: {books[ind]}')
        print("Приятного чтения!\n\n")
    elif user_input == '3':
        books = nurzhan.get_book()

        if not books:
            print("У вас нет взятых книг.\n")
        else:
            for i in range(len(books)):
                print(f"{i}. {books[i]}")
            ind = int(input("Возвращайте книгу: "))
            nurzhan.return_book(books[ind])
            print("Спасибо!\n\n")
            # проверить какие книги взял
    elif user_input == '4':
        books = nurzhan.get_book()
        if not books:
            print("У вас нет взятых книг.\n")
        else:
            print("Ваши взятые книги:\n")

            for i, book in enumerate(books, start=1):
                print(f"{i}. {book}")
            print()

    elif user_input == '5':
        books = nurzhan.get_book()
        if not books:
            print("У вас нет взятых книг.\n")
        else:
            for i in range(len(books)):
                print(f"{i}. {books[i]}")
            ind = int(input("Возвращайте книгу: "))
            nurzhan.return_book(books[ind])
            print("Спасибо!\n\n")
    elif user_input == 'q':
        print("До свидания!")
