from typing import Callable, Dict, List, TypeVar

from peewee import ModelSelect

from database.common.models import ModelBase
from ..common.models import db


T = TypeVar('T')


class _Store():
    """
    Базовый класс. Здесь происходит запись данных в БД.
    """
    def store_data(db: db, model: T, *data: List[Dict]) -> None:

        with db.atomic():
            model.insert_many(*data).execute()


class _Retrieve():
    """
    Базовый класс. Здесь происходит чтение данных из БД.
    """
    def retrieve_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:

        with db.atomic():
            response = model.select(*columns)

        return response


class CRFactory():
    """
    Класс-фабрика. Работает с инкапсулированными классами чтения и записи в БД.

    Поля:
    CRUD (dict): словарь, где ключи - название команды для метода фабрики, значения - ссылка на метод нужного класса
    """
    CRUD = {
        "store": _Store.store_data,
        "retrieve": _Retrieve.retrieve_data
    }

    @classmethod
    def handle(cls, command: str, db: db, model: T, *args) -> Callable:

        method = cls.CRUD.get(command)

        if method:
            return method(db, model, *args)


if __name__ == "__main__":

    CRFactory()
