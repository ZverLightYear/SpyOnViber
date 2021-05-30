from core.zlog.zlog import Zlog

from sqlalchemy import inspect
from sqlalchemy.sql.expression import or_, select
from sqlalchemy.exc import OperationalError

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
        Инициализация контроллера БД Viber.
        :param db_conf: конфигурация БД Viber.
        """
        super().__init__(db_conf)
        # задаем правила обращения к моделям БД Viber.
        self.select_by_model = {
            Chat.__tablename__: select(Chat),
            Contact.__tablename__: select(Contact),
            ChatRelation.__tablename__: select(ChatRelation),
            Event.__tablename__: select(Event),
            Message.__tablename__: select(Message, Event).join(Event, Event.EventID == Message.EventID)
        }

    def create_tables_with_check(self):
        """
        Заглушка создания таблиц БД Viber.
        Запрещаем любое активное вмешательство в БД Viber.
        :return: raise OperationalError
        """
        Zlog.error(f"Don't touch Viber database, please!")
        raise OperationalError(None, None, None)

    def drop_tables(self):
        """
        Заглушка удаления таблиц БД Viber.
        Запрещаем любое активное вмешательство в БД Viber.
        :return: raise OperationalError
        """
        Zlog.error(f"Don't touch Viber database, please!")
        raise OperationalError(None, None, None)

    def get_new_rows(self, model, pk_last_values):
        """
        Получить список "новых" строк модели Viber.
        :param model: модель, для которых необходимо получить список новых строк.
        :param pk_last_values: значения для primary key модели. Определяют новизну строк.
        :return: список новых строк модели.
        """
        pk = inspect(model).primary_key
        query = self.select_by_model[model.__tablename__]
        query = query.where(or_(pk[i] > pk_last_values[i] for i in range(len(pk))))
        return self.engine.execute(query).fetchall()
