from core.zlog.zlog import Zlog

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
        Инициализация контроллера БД.
        :param db_conf: конфигурация БД Viber.
        """
        super().__init__(db_conf)
        self.select_by_model = {
            Chat.__tablename__: select(Chat),
            Contact.__tablename__: select(Contact),
            ChatRelation.__tablename__: select(ChatRelation),
            Event.__tablename__: select(Event),
            Message.__tablename__: select(Message, Event).join(Event, Event.EventID == Message.EventID)
        }

    def create_tables_with_check(self):
        Zlog.error(f"Don't touch Viber database, please.")
        raise OperationalError

    def drop_tables(self):
        Zlog.error(f"Don't touch Viber database, please.")
        raise OperationalError

    def get_new_rows(self, model, pk, pk_last_values):
        query = self.select_by_model[model.__tablename__]
        query = query.where(or_(pk[i] > pk_last_values[i] for i in range(len(pk))))
        return self.engine.execute(query).fetchall()
