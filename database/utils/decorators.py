from typing import Callable, TypeVar

from database.utils.CRUD import CRFactory
from database.common.models import db


T = TypeVar('T')

class CRUDParameters():
    """
    Класс-декоратор. Выполняет функцию сведения к минимуму дублирования кода по запросам к базе данных.
    Обязательное условие: декорируемый класс должен быть дочерним классом CRFactory.
    """
    def __init__(self, command: str, db: db, model: T, *args) -> None:
        self.command = command
        self.db = db
        self.model = model
        self.args = *args,

    def __call__(self, object: CRFactory) -> Callable:
        return object.handle(self.command, self.db, self.model, *self.args)


if __name__ == "__main__":

    CRUDParameters
