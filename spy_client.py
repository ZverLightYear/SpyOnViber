import json

from core.viber_db_controller import ViberDatabaseController
from core.app_db_controller import ApplicationDatabaseController

from core.models.app.chat import Chat
from core.models.app.contact import Contact
from core.models.app.chat_relation import ChatRelation
from core.models.app.message import Message


def install_app_db(app_engine):
    Chat.__table__.create(app_engine, checkfirst=True)
    Contact.__table__.create(app_engine, checkfirst=True)
    ChatRelation.__table__.create(app_engine, checkfirst=True)
    Message.__table__.create(app_engine, checkfirst=True)

def drop_app_db(app_engine):
    Message.__table__.drop(app_engine, checkfirst=True)
    ChatRelation.__table__.drop(app_engine, checkfirst=True)
    Contact.__table__.drop(app_engine, checkfirst=True)
    Chat.__table__.drop(app_engine, checkfirst=True)


if __name__ == '__main__':
    conf = json.load(open(r"conf.json"))
    database_conf = conf["database"]

    viber_db_conf = database_conf["viber_db"]
    app_db_conf = database_conf["app_db"]

    viber_db = ViberDatabaseController(viber_db_conf)
    app_db = ApplicationDatabaseController(app_db_conf)

    viber_db.connect()
    app_db.connect()

    drop_app_db(app_dbc.engine)
    install_app_db(app_dbc.engine)

    viber_db.close()
    app_db.close()
