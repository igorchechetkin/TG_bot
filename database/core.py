from database.common.models import db, PlayersHistory, TeamsHistory
from database.utils.CRUD import CRFactory
from database.utils.decorators import CRUDParameters
from site_API.core import RequestsFactory


db.connect()
db.create_tables([PlayersHistory])
db.create_tables([TeamsHistory])


site_api = RequestsFactory
db_request = CRUDParameters
crud = CRFactory


@db_request("store", db, PlayersHistory, site_api.site_api_handle("players"))
class DBStorePlayers(CRFactory):
    """
    Дочерний класс, записывает данные об игроках в БД. Родитель CRFactory. Принимает данные из запроса к сайту,
    прогоняет через декоратор CRUDParameters и дальнейшая работа происходит в родительском классе.
    """
    pass


@db_request("store", db, TeamsHistory, site_api.site_api_handle("teams"))
class DBStoreTeams(CRFactory):
    """
    Дочерний класс, записывает данные о командах в БД. Родитель CRFactory. Принимает данные из запроса к сайту,
    прогоняет через декоратор CRUDParameters и дальнейшая работа происходит в родительском классе.
    """
    pass


@db_request("retrieve", db, PlayersHistory, PlayersHistory.id, PlayersHistory.first_name, PlayersHistory.last_name)
class DBRetrievePlayers(CRFactory):
    """
    Дочерний класс, отдает данные об игроках из БД. Родитель CRFactory. Прогоняет через декоратор CRUDParameters
    и дальнейшая работа происходит в родительском классе.
    """
    pass


@db_request("retrieve", db, TeamsHistory, TeamsHistory.id, TeamsHistory.conference, TeamsHistory.full_name)
class DBRetrieveTeams(CRFactory):
    """
    Дочерний класс, читает данные о командах из БД. Родитель CRFactory. Прогоняет через декоратор CRUDParameters,
    и дальнейшая работа происходит в родительском классе.
    """
    pass


class DBFactory():
    """
    Класс-фабрика. Организует работу классов, которые взаимодействуют с базой данных.

    Attrs:
    STORED (dict): словарь объектов записи в БД. Где ключ - команда, значение - объект, осуществляющий
                   запись в нужную таблицу

    RETRIEVED (dict): словарь объектов чтения из БД. Где ключ - команда, значение - объект, осуществляющий
                      чтение из нужной таблицы
    """
    STORED = {
        "db_players": DBStorePlayers,
        "db_teams": DBStoreTeams
    }

    RETRIEVED = {
        "db_players": DBRetrievePlayers,
        "db_teams": DBRetrieveTeams
    }

    @classmethod
    def handle(cls, command: str):
        """
        Метод класса-фабрики. Принимает команду в качестве аргумента, далее из атрибутов, по названию команды,
        достает ссылку на нужный класс для работы с данными. Работа программы продолжается в этих классах.

        :param command (str): команда на получения из атрибутов класса нужной ссылки на объект
        :return: data
        """
        cls.STORED.get(command)

        data = cls.RETRIEVED.get(command)

        if data:
            return data


if __name__ == "__main__":

    DBFactory()
