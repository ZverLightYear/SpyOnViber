import json
from core.db_controller import DatabaseController
from core.viber_db_controller import ViberDatabaseController


if __name__ == '__main__':
    conf = json.load(open(r"conf.json"))
    database_conf = conf["database"]

    viber_db_conf = database_conf["viber_db"]
    app_db_conf = database_conf["app_db"]

    viber_db = ViberDatabaseController(viber_db_conf)
    app_db = DatabaseController(app_db_conf)

    viber_db.connect()
    app_db.connect()

    # ToDo

    viber_db.close()
    app_db.close()
