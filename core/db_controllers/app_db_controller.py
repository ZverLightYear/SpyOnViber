from core.zlog.zlog import Zlog

from sqlalchemy import inspect
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
        """
        Создание таблиц БД приложения с проверкой на их существование.
        """
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
        """
        Удаление таблиц БД приложения.
        """
        Zlog.warning("Dropping tables in database.")
        try:
            self.connect()
            Message.__table__.drop(self.engine, checkfirst=True)
            ChatRelation.__table__.drop(self.engine, checkfirst=True)
            Contact.__table__.drop(self.engine, checkfirst=True)
            Chat.__table__.drop(self.engine, checkfirst=True)
            self.disconnect()
            Zlog.warning("Tables in the database were dropped successfully.")
        except Exception as err:
            Zlog.error(f"Error dropping tables in the database: {err}")

    def get_last_model_id(self, model):
        """
        Получить набор последних (больших) primary key для модели.
        :param model: модель, для которой возвращается набор primary key.
        :return: набор последних (больших) primary key.
        """
        model_pk = inspect(model).primary_key
        with self.session() as sess:
            return [sess.query(func.max(pk))[0][0] or 0 for pk in model_pk]

    def insert_bulk_rows(self, insertion):
        """
        Добавить набор записей в модель БД приложения.
        :param insertion: набор добавляемых записей.
        :return:
        """
        with self.session.begin() as sess:
            sess.bulk_save_objects(insertion)
            sess.commit()
