import json

from core.db_controllers.viber_db_controller import ViberDatabaseController
from core.db_controllers.app_db_controller import ApplicationDatabaseController

from core.adapters.viber_to_app.viber_to_app_database_adapter import ViberToAppDatabaseAdapter

if __name__ == '__main__':
    conf = json.load(open(r"conf.json"))
    databases_conf = conf["databases"]

    viber_db_conf = databases_conf["viber_db"]
    app_db_conf = databases_conf["app_db"]

    viber_dbc = ViberDatabaseController(viber_db_conf)
    app_dbc = ApplicationDatabaseController(app_db_conf)

    app_dbc.drop()
    app_dbc.create()

    v2a_db_adapter = ViberToAppDatabaseAdapter(viber_dbc, app_dbc)
    v2a_db_adapter.translate_chat()
    v2a_db_adapter.translate_contact()
    v2a_db_adapter.translate_chat_relation()
    v2a_db_adapter.translate_message()

    viber_dbc.disconnect()
    app_dbc.disconnect()
