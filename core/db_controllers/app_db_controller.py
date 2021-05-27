from sqlalchemy import select
from sqlalchemy.sql.expression import func

from core.db_controllers.db_controller import DatabaseController

from core.models.app.chat import Chat
from core.models.app.contact import Contact
from core.models.app.chat_relation import ChatRelation
from core.models.app.message import Message


class ApplicationDatabaseController(DatabaseController):
    """
    Реализация контроллера БД для работы с БД приложения.
    """

    def __init__(self, db_conf):
        """
        Инициализация контроллера БД.
        :param db_conf: конфигурация БД приложения.
        """
        super().__init__(db_conf)

    def create(self):
        self.connect()
        Chat.__table__.create(self.engine, checkfirst=True)
        Contact.__table__.create(self.engine, checkfirst=True)
        ChatRelation.__table__.create(self.engine, checkfirst=True)
        Message.__table__.create(self.engine, checkfirst=True)
        self.disconnect()

    def drop(self):
        self.connect()
        Message.__table__.drop(self.engine, checkfirst=True)
        ChatRelation.__table__.drop(self.engine, checkfirst=True)
        Contact.__table__.drop(self.engine, checkfirst=True)
        Chat.__table__.drop(self.engine, checkfirst=True)
        self.disconnect()

    def get_chat_list(self):
        return self.execute_with_session(select(Chat))

    def get_last_chat_id(self):
        with self.session() as sess:
            return sess.query(func.max(Chat.ChatID))[0][0] or 0

    def get_contact_list(self):
        return self.execute_with_session(select(Contact))

    def get_last_contact_id(self):
        with self.session() as sess:
            return sess.query(func.max(Contact.ContactID))[0][0] or 0

    def get_message_list(self):
        return self.execute_with_session(select(Message))

    def get_last_message_id(self):
        with self.session() as sess:
            return sess.query(func.max(Message.MessageID))[0][0] or 0

    def get_chat_relation_list(self):
        return self.execute_with_session(select(ChatRelation))

    def get_last_chat_relation_id(self):
        with self.session() as sess:
            return sess.query(func.max(Message.MessageID))[0][0] or 0

    def insert_chat(self, chat):
        with self.session.begin() as sess:
            sess.add(chat)
            sess.commit()

    def insert_chat_list(self, chat_list):
        with self.session.begin() as sess:
            sess.bulk_save_objects(chat_list)
            sess.commit()

    def insert_contact(self, contact):
        with self.session.begin() as sess:
            sess.add(contact)
            sess.commit()

    def insert_contact_list(self, contact_list):
        with self.session.begin() as sess:
            sess.bulk_save_objects(contact_list)
            sess.commit()

    def insert_message(self, message):
        with self.session.begin() as sess:
            sess.add(message)
            sess.commit()

    def insert_message_list(self, message_list):
        with self.session.begin() as sess:
            sess.bulk_save_objects(message_list)
            sess.commit()

    def insert_chat_relation(self, chat_relation):
        with self.session.begin() as sess:
            sess.add(chat_relation)
            sess.commit()

    def insert_chat_relation_list(self, chat_relation_list):
        with self.session.begin() as sess:
            sess.bulk_save_objects(chat_relation_list)
            sess.commit()
