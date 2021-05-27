from sqlalchemy import select

from core.db_controllers.db_controller import DatabaseController

from core.models.viber.message import Message
from core.models.viber.contact import Contact
from core.models.viber.chat import Chat
from core.models.viber.chat_relation import ChatRelation
from core.models.viber.event import Event


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

    def create(self):
        pass

    def drop(self):
        pass

    def get_chat_list(self):
        return self.execute_with_session(Chat)

    def get_contact_list(self):
        return self.execute_with_session(Contact)

    def get_message_list(self):
        return self.execute_with_session(Message)

    def get_chat_relation_list(self):
        return self.execute_with_session(ChatRelation)

    def get_message_list_v2(self):
        with self.session() as sess:
            query = sess.query(Message, Event)
            query = query.join(Event, Event.EventID == Message.EventID)
            print(query)
            records = query.all()
            return records


