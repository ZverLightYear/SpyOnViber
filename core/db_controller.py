from __future__ import annotations
from abc import abstractmethod, ABC

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


class DatabaseController(ABC):
    """
    Интерфейс контроллера БД.
    Объявляет операции, которые должны выполнять все контроллеры БД.
    """
    @abstractmethod
    def __init__(self, db_conf):
        """
        Инициализация контроллера БД.
        :param db_conf: конфигурация используемой БД.
        """
        self.engine = None
        self.db_conf = db_conf

    @staticmethod
    def __conf_to_url(db_conf):
        """
        Генератор connection-string для подключения к БД.
        :param db_conf: параметры подключения к БД.
        :return: connection-string для подключения к БД.
        """
        engine = db_conf.get('ENGINE')
        user = db_conf.get('USER', None)
        password = db_conf.get('PASSWORD', None)
        host = db_conf.get('HOST', None)
        port = db_conf.get('PORT', None)
        db_name = db_conf.get('DB_NAME')

        return URL(engine, user, password, host, port, db_name)

    def connect(self):
        """
        Подключение к БД с созданием сессии.
        """
        self.engine = create_engine(self.__conf_to_url(self.db_conf), echo=True)

    def close(self):
        """
        Закрытие подключения к БД.
        """
        del self.engine
        self.engine = None
