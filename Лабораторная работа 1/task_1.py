# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

# класс 1
class Song:
    """
    Документация на класс. Класс описывает песню.
    """
    def __init__(self, music_artist: str, name_of_song: str, year: int):
        """
        Создание и подготовка к работе объекта "Песня"

        :param music_artist: Имя исполнителя
        :param name_of_song: Название песни
        :param year: Год выпуска

        Пример:
        >>> song = Song("Adele", "Skyfall", 2012) # инициализация экземпляра класса
        """
        if not isinstance(music_artist, str):
            raise TypeError("Имя исполнителя должно быть типа str")
        self.music_artist = music_artist

        if not isinstance(name_of_song, str):
            raise TypeError("Название песни должно быть типа str")
        self.name_of_song = name_of_song

        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть типа int")
        if year< 0:
            raise ValueError("Год выпуска должен быть положительным числом")
        self.year = year

    def song_of_20th_century(self) -> bool:
        """
        Функция, которая проверяет, является ли песня выпущенной в 20-м веке

        :return: Выпущена ли песня в 20-м веке

        Примеры:
        >>> song = Song("Adele", "Skyfall", 2012)
        >>> song.song_of_20th_century()
        """
        ...

    def song_in_russian(self) -> bool:
        """
        Функция, которая проверяет, является ли песня песней на русском языке

        :return: Исполняется ли песня на русском языке
        Примеры:
        >>> song = Song("Маяк", "Воспоминание", 2022)
        >>> song.song_in_russian()
        """
        ...

# класс 2
class Day:
    """
    Документация на класс. Класс описывает день тремя словами.
    """
    def __init__(self, three_words: list, score: int):
        """
        Создание и подготовка к работе объекта "День"

        :param three_words: Три слова, описывающие ваш день
        :param score: Оценка дня

        Пример:
        >>> day1 = Day(["свободный", "интересный", "долгий"], 5)
        """
        if not isinstance(three_words, list):
            raise TypeError("Три слова должны быть типа list")
        if len(three_words) != 3:
            raise ValueError("В списке должно быть три элемента")
        self.three_words = three_words

        if not isinstance(score, int):
            raise TypeError("Оценка должна быть типа int")
        if score != 1 and score != 2 and score != 3 and score != 4 and score != 5:
            raise ValueError("Оценка должна быть от 1 до 5")
        self.score = score

    def add_word(self, word: str) -> None:
        """
        Добавление слова в список

        :param word: Добавляемое слово
        :return: Новый список

        Пример:
        >>> day1 = Day(["свободный", "интересный", "долгий"], 5)
        >>> day1.add_word("слово")
        """
        if not isinstance(word, str):
            raise TypeError("Добавляемое слово должно быть типа str")
        ...

    def check_score(self) -> bool:
        """
        Функция, которая проверяет, что оценка дня выше 3

        :return: Выше ли оценка дня 3-х баллов?

        Примеры:
        >>> day1 = Day(["свободный", "интересный", "долгий"], 5)
        >>> day1.check_score()
        """
        ...

# класс 3
class Exam:
    """
    Документация на класс. Класс описывает экзамены.
    """
    def __init__(self, subject: str, number_of_questions: int):
        """
        Создание и подготовка к работе объекта "Экзамен"

        :param subject: Предмет
        :param number_of_questions: Количество вопросов

        Пример:
        >>> exam1 = Exam("Высшая математика", 30)
        """
        if not isinstance(subject, str):
            raise TypeError("Предмет должен быть типа str")
        self.subject = subject

        if not isinstance(number_of_questions, int):
            raise TypeError("Количество вопросов должно быть типа int")
        if number_of_questions <= 0:
            raise ValueError("Количество вопросов не может быть отрицательным числом или нулем")
        if number_of_questions < 10:
            raise ValueError("Минимальное число вопросов к экзамену 10")
        self.number_of_questions = number_of_questions

    def check_if_more_than_20(self) -> bool:
        """
        Функция, которая проверяет, что количество вопросов к экзамену превышает 20

        :return: Вопросов к экзамену больше 20?

        Примеры:
        >>> exam1 = Exam("Высшая математика", 30)
        >>> exam1.check_if_more_than_20()
        """
        ...

    def add_questions(self, number_of_additional_questions: int) -> None:
        """
        Добавление новых вопросов к экзамену
        :param number_of_additional_questions: Дополнительные вопросы

        :return: Количество дополнительных вопросов

        Примеры:
        >>> exam1 = Exam("Высшая математика", 30)
        >>> exam1.add_questions(5)
        """
        if not isinstance(number_of_additional_questions, int):
            raise TypeError("Количество дополнительных вопросов должно быть типа int")
        if number_of_additional_questions < 0:
            raise ValueError("Количество дополнительных вопросов не может быть отрицательным")
        ...





if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod() # тестирование примеров, которые находятся в документации
