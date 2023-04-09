import os

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr, StrictInt, StrictStr

load_dotenv()


class SiteSettings(BaseSettings):
    """
    Базовый класс настроек для сайта, с которого будут парситься данные

    Поля:
    api_key (str): Получает данные из файла .env с ключом API сайта
    api_host (str): Получает данные из файла .env с хостом сайта
    api_timeout (int): Базовый таймаут

    """
    api_key: SecretStr = os.getenv("API_KEY", None)
    api_host: StrictStr = os.getenv("API_HOST", None)
    api_timeout: StrictInt = os.getenv("API_TIMEOUT", 10)


class BotSettings(BaseSettings):
    """
    Базовый класс настроек чувствительных данных телеграм бота

    Поля:
    token (str): Токен доступа к телеграм боту. Получаем из файла .env
    """
    token: SecretStr = os.getenv("BOT_TOKEN", None)


class ApiFields(BaseSettings):
    """
    Базовый класс для работы с полями данных в датаклассе

    Поля:
    fields_players (str): Передается строка с предполагаемыми данными об игроках, которую в дальнейшем преобразовываем
                          в список ключевых слов, по которым происходит отбор данных из словаря, полученного
                          с помощью датакласса
    fields_teams (str): Передается строка с предполагаемыми данными о командах, которую в дальнейшем преобразовываем
                        в список ключевых слов, по которым происходит отбор данных из словаря, полученного
                        с помощью датакласса
    """
    fields_players: StrictStr = os.getenv("FIELDS_PLAYERS", None)
    fields_teams: StrictStr = os.getenv("FIELDS_TEAMS", None)
