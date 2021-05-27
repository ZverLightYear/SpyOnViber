from core.db_controller import DatabaseController
from core.models.viber.message import Message

from sqlalchemy import select


class ViberDatabaseController(DatabaseController):
    """
    Реализация контроллера БД для работы с БД Viber.
    """
    def __init__(self, db_conf):
        """
        Инициализация контроллера БД.
        :param db_conf: конфигурация БД Viber.
        """
        super().__init__(db_conf)

    def select_mesages(self):
        with self.engine.connect() as connection:
            result = connection.execute(select(Message))

            for r in result:
                print(r.Body)
