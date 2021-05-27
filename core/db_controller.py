from __future__ import annotations
from abc import abstractmethod, ABC
from sqlalchemy import create_engine
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

    @staticmethod
    def __conf_to_connection_string(db_conf):
        """
        Генератор connection-string для подключения к БД.
        :param db_conf: параметры подключения к БД.
        :return: connection-string для подключения к БД.
        """
        user = db_conf.get('USER', '')
        password = db_conf.get('PASSWORD', '')
        host = db_conf.get('HOST', '')
        engine = db_conf.get('ENGINE')
        db_name = db_conf.get('DB_NAME')

        # Если пользователь объявлен, то необходимо разделить аутентификационные данные от хоста
        #   перед хостом ставим @
        # Если пользователь НЕ объявлен, то пароль не используется
        if user:
            host = f'@{host}'
        else:
            password = ''

        # Если пароль для пользователя объявлен, то необходимо разделить логин и пароль
        #   между логином и паролем ставим :
        if user and password:
            password = f':{password}'

        # print(f"{engine}://{user}{password}{host}/{db_name}")
        return f"{engine}://{user}{password}{host}/{db_name}"

    def connect(self):
        """
        Подключение к БД с созданием сессии.
        """
        self.engine = create_engine(self.__conf_to_connection_string(self.db_conf), echo=True)
        self.session = sessionmaker(bind=self.engine)()

    def close(self):
        """
        Закрытие подключения к БД.
        """
        self.session.close()
        del self.session
        del self.engine
        self.engine = None
        self.session = None
