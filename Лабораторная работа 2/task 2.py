BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    """
    Документация на класс. Класс описывает книгу.
    """
    def __init__(self, id_: int, name: str, pages: int):
        """
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книги должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


# TODO написать класс Library
class Library:
    """
    Документация на класс. Класс описывает библиотеку.
    """
    def __init__(self, books=[]):
        """
        :param books: Список книг
        """
        self.books = books

    def get_next_book_id(self):
        """
        Функция, которая возвращает идентификатор для добавления новой книги в библиотеку.
        :return: Идентификатор (id)
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1 #вызываем атрибут id_ последнего элемента с списке и увеличиваем его на 1

    def get_index_by_book_id(self, book_id):
        """
        Функция, которая возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса.

        :param book_id: Идентификатор книги (id)
        :return: Индекс книги в списке
        """
        for index, book in enumerate(self.books): # используем функцию enumerate для получения пар индекс-значение
            if book_id == book.id_:
                return index
            else:
                raise ValueError("Книги с запрашиваемым id не существует")




if __name__ == '__main__':

    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1


