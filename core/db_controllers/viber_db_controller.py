from sqlalchemy.sql.expression import or_

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

    def create_with_check(self):
        pass

    def drop(self):
        pass

    def get_chat_list(self, condition=None):
        return self.execute_with_session(Chat)

    def get_new_chat_list(self, last_id=0):
        with self.session() as sess:
            return sess.query(Chat).where(Chat.ChatID > last_id).all()

    def get_contact_list(self):
        return self.execute_with_session(Contact)

    def get_new_contact_list(self, last_id=0):
        with self.session() as sess:
            return sess.query(Contact).where(Contact.ContactID > last_id).all()

    def get_message_list(self):
        return self.execute_with_session(Message)

    def get_message_list_v2(self):
        with self.session() as sess:
            query = sess.query(Message, Event)
            query = query.join(Event, Event.EventID == Message.EventID)
            records = query.all()
            return records

    def get_new_message_list_v2(self, last_id=0):
        with self.session() as sess:
            query = sess.query(Message, Event)
            query = query.join(Event, Event.EventID == Message.EventID)
            query = query.where(Message.EventID > last_id)
            records = query.all()
            return records

    def get_chat_relation_list(self):
        return self.execute_with_session(ChatRelation)

    def get_new_chat_relation_list(self, last_chat_id=0, last_contact_id=0):
        with self.session() as sess:
            return sess.query(ChatRelation). \
                where(or_(ChatRelation.ChatID > last_chat_id,
                          ChatRelation.ContactID > last_contact_id)). \
                all()

