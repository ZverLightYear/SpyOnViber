from core.zlog.zlog import Zlog

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

    def create_tables_with_check(self):
        Zlog.info("Create tables in the database.")
        try:
            self.connect()
            Chat.__table__.create(self.engine, checkfirst=True)
            Contact.__table__.create(self.engine, checkfirst=True)
            ChatRelation.__table__.create(self.engine, checkfirst=True)
            Message.__table__.create(self.engine, checkfirst=True)
            self.disconnect()
            Zlog.info("Tables in the database were created successfully.")
        except Exception as err:
            Zlog.error(f"Error creating tables in the database: {err}")

    def drop_tables(self):
        Zlog.warning("Dropping tables in database.")
        try:
            self.connect()
            Message.__table__.drop_tables(self.engine, checkfirst=True)
            ChatRelation.__table__.drop_tables(self.engine, checkfirst=True)
            Contact.__table__.drop_tables(self.engine, checkfirst=True)
            Chat.__table__.drop_tables(self.engine, checkfirst=True)
            self.disconnect()
            Zlog.warning("Tables in the database were dropped successfully.")
        except Exception as err:
            Zlog.error(f"Error dropping tables in the database: {err}")

    def get_last_model_id(self, model_pk):
        with self.session() as sess:
            return sess.query(func.max(model_pk))[0][0] or 0

    def insert_bulk_rows(self, insertion):
        with self.session.begin() as sess:
            sess.bulk_save_objects(insertion)
            sess.commit()
