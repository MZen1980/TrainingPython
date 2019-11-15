import random
from typing import Optional, Any, Union, List, Tuple, Iterable, Dict


class Character:
    # прописываем ожидаемые типы что бы потом когда мы ожидаем число нам не сували строку
    def __init__(self, armor: int, power: int):
        self.armor = armor
        self.power = power
        self.health = 100


def hit(self, damage: int):
    self.health -= damage


def is_alive(self) -> bool:  # теперь истема знает что функция возвращает булево
    return self.health > 0


c1 = Character(10, 20)
c1.hit(20)  # выйдет ошибка что бы такого не было прописывать надо типы
print(c1.health)

amount: int
amount = None

price: Optional[int]  # что бы линтер не ругался импортируем Optional
price = 10  # можем добавлять числа , None
price = None
price = "day bau"

attack: Any = 1  # при таком импорте можем добавлять значения любых типов
attack = "1"

length: Union[int, float]  # импортируем и покажем что используем целые и дробные числа
length = 1
length = 1.23
length = 'adasd'  # на str уже ругается

quotes: list
quotes = "asdd"

quotes: List[int]  # Set, FrozenSet
quotes.append(1)
quotes.append("aasdf")

player: Tuple[str, int] = ("Kramnik", 2750)

changes_in_rating: Tuple[int, ...]  # пропишем что в Tuple только числа
changes_in_rating = (1, 2, 3, 4, 5)
changes_in_rating = (1, "adaff")  # как видно на str ругается

chess_players: Dict[str, int] = {"Kramnik": 2750}  # DefaultDict is also available


# скажем что из функции возвращается оперируемый объект
def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)
