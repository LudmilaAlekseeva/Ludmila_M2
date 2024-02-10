class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс - Бумажная книга. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages (self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages<=0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Бумажная книга '{self.name}'. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """ Дочерний класс - Аудио-книга. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name,author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration (self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудио-книги должна быть типа float")
        if new_duration<=0:
            raise ValueError("Продолжительность аудио-книги не может быть отрицательной")
        self._duration = new_duration

    def __str__(self):
        return f"Аудио-книга '{self.name}'. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

book = Book("Евгений Онегин", "А. С. Пушкин") # экземпляр класса Book для проверки
paper_book = PaperBook("Мертвые души", "Н. В. Гоголь", 350) # экземпляр класса PaperBook для проверки
audio_book = AudioBook("Метель", "А. С. Пушкин", 57.8) # экземпляр класса AudioBook для проверки

# проверка работы программы
print(book.name)
print(paper_book.pages)
paper_book.pages = 100
print(paper_book.pages)
print(audio_book)
print(audio_book.duration)
audio_book.duration = 60.0
print(audio_book.duration)