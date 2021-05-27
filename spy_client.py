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
    databases_conf = conf["databases"]

    viber_db_conf = databases_conf["viber_db"]
    app_db_conf = databases_conf["app_db"]

    viber_dbc = ViberDatabaseController(viber_db_conf)
    app_dbc = ApplicationDatabaseController(app_db_conf)

    viber_dbc.connect()
    app_dbc.connect()

    drop_app_db(app_dbc.engine)
    install_app_db(app_dbc.engine)

    # viber_dbc.select_mesages()
    # app_dbc.query()

    viber_dbc.close()
    app_dbc.close()
