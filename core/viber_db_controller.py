from sqlalchemy import select

from core.db_controller import DatabaseController

from core.models.viber.message import Message
from core.models.viber.contact import Contact
from core.models.viber.chat import Chat
from core.models.viber.event import Event
from core.models.viber.chat_relation import ChatRelation


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

    def get_messages_list(self):
        return self.query(select(Message))

    def get_contact_list(self):
        return self.query(select(Contact))
