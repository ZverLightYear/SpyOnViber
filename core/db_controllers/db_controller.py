from __future__ import annotations
from abc import abstractmethod, ABC

from core.zlog.zlog import Zlog

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


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
        self.session = None
        self.db_conf = db_conf
        self.url = URL(**self.db_conf)

    @abstractmethod
    def create_with_check(self):
        """
        Создание таблиц БД.
        """
        pass

    @abstractmethod
    def drop(self):
        """
        Удаление таблиц БД
        """
        pass

    def connect(self):
        """
        Подключение к БД с созданием сессии.
        """
        Zlog.info(f"Connecting to database {self.url} ...", end='')
        try:
            self.engine = create_engine(self.url)
            self.session = sessionmaker(self.engine)
            Zlog.info("[OK]", without_prefix=True)
        except Exception as err:
            Zlog.error(f"[FAIL] {err}", without_prefix=True)

    @abstractmethod
    def get_contact_list(self):
        """
        Полуение списка всех контактов.
        :return: список контактов.
        """
        pass

    @abstractmethod
    def get_chat_list(self):
        """
        Полуение списка всех чатов.
        :return: список чатов.
        """
        pass

    @abstractmethod
    def get_message_list(self):
        """
        Полуение списка всех сообщений.
        :return: список сообщений.
        """
        pass

    @abstractmethod
    def get_chat_relation_list(self):
        """
        Полуение списка всех связей контактов с чатами.
        :return: список связей контактов с чатами.
        """
        pass

    def execute_with_session(self, query):
        """
        Выполнить запрос с открытием сессии.
        :param query: запрос.
        :return: результат выполнения запроса.
        """
        with self.session() as sess:
            return sess.query(query).all()

    def disconnect(self):
        """
        Закрытие подключения к БД с закрытием сессии.
        """
        Zlog.info(f"Disconnecting database {self.url} ...", end='')
        try:
            del self.session
            self.session = None
            del self.engine
            self.engine = None
            Zlog.info("[OK]", without_prefix=True)
        except Exception as err:
            Zlog.error(f"[FAIL] {err}", without_prefix=True)
