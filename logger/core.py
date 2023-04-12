import logging
from typing import Callable


class Logged():
    """
    Класс-декоратор логирования.
    В DEBUG логируются все действия программы.
    В INFO логируем все взаимодействия пользователя с ботом
    Остальные уровни логируются на системном уровне.
    """
    logging.basicConfig(level=logging.DEBUG, filename="logger.log", filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")

    def __call__(self, object: Callable) -> Callable:
        return object


if __name__ == "__main__":

    Logged
