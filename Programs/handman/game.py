import random
from typing import Iterable, List

from handman.game_status import GameStatus
from handman.invalid_operation_exception import InvalidOperationException


class Game:
    def __init__(self, allowed_misses: int = 6):
        if allowed_misses < 5 or allowed_misses > 8:
            raise ValueError("Number of allowed misses should be between 5 and 8.")
        self.__allowed_misses = allowed_misses  # кол-во попыток
        self.__tries_counter = 0  # счетчик попыток
        self.__tried_letters = []  # какие буквы были опробованы
        self.__open_indexes = []  # список не открытых букв
        self.__game_status = GameStatus.NOT_STARTED  # статус игры
        self.__word = ""

    @property
    def generate_word(self) -> str:
        filename = "C:\\Users\\Михаил и Натусик\\GitHub\\TrainingPython\\Programs\\handman\\data\\WordsStockRus.txt"

        words = []  # слова зпишем сюда
        with open(filename, encoding='utf8') as file:
            for line in file:
                words.append(line.strip('\n'))

        # выберем случайно слово из списка
        rand_index = random.randint(0, len(words) - 1)

        self.__word = words[rand_index]

        self.__open_indexes = [False for _ in self.__word]
        self.__game_status = GameStatus.IN_PROGRESS

        # возвращаем слово
        return self.__word

    def guess_letter(self, letter: str) -> Iterable[str]:
        if self.tries_counter == self.allowed_misses:
            raise InvalidOperationException(f'Exceeded the max misses number. Allowed {self.allowed_misses}')

        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationException(f'Inappropriate status of game: {self.game_status}')
        open_any = False
        result: List[str] = []

        for i in range(len(self.word)):
            cur_letter = self.word[i]
            if cur_letter == letter:
                self.__open_indexes[i] = True
                open_any = True

            if self.__open_indexes[i]:
                result.append(cur_letter)
            else:
                result.append('-')

        if not open_any:
            self.__tries_counter += 1

        self.__tried_letters.append(letter)

        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.tries_counter == self.allowed_misses:
            self.__game_status = GameStatus.LOST

        return result

    def __is_winning(self):
        for cur in self.__open_indexes:
            if not cur:
                return False
        return True

    # Ограничим доступ внешнего кода к нашим атрибутам
    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def word(self) -> str:
        return self.__word

    @property
    def allowed_misses(self) -> int:
        return self.__allowed_misses

    @property
    def tries_counter(self) -> int:
        return self.__tries_counter

    @property
    def tried_letters(self) -> Iterable[str]:
        return sorted(self.__tried_letters)

    @property
    def remaining_tries(self) -> int:
        return self.allowed_misses - self.tries_counter
