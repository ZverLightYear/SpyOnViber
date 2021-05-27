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

    def connect(self):
        """
        Подключение к БД с созданием сессии.
        """
        self.engine = create_engine(URL(**self.db_conf), echo=True)

    def query(self, query):
        with self.engine.connect() as connection:
            return connection.execute(query)

    def close(self):
        """
        Закрытие подключения к БД.
        """
        del self.engine
        self.engine = None
