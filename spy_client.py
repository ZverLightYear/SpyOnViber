import json
import time
from core.zlog.zlog import Zlog

from core.db_controllers.viber_db_controller import ViberDatabaseController
from core.db_controllers.app_db_controller import ApplicationDatabaseController

from core.adapters.viber_to_app.viber_to_app_database_adapter import ViberToAppDatabaseAdapter

if __name__ == '__main__':
    conf = json.load(open(r"conf.json"))

    logging_conf = conf["settings"]["logging"]
    Zlog.logLevel = logging_conf["level"]

    databases_conf = conf["databases"]
    Zlog.info("Startup config:")
    Zlog.info(json.dumps(databases_conf, indent=4))

    sleep_time = conf["settings"]["process_sleep_time"]

    viber_db_conf = databases_conf["viber_db"]
    app_db_conf = databases_conf["app_db"]

    viber_dbc = ViberDatabaseController(viber_db_conf)
    app_dbc = ApplicationDatabaseController(app_db_conf)

    # app_dbc.drop()
    # app_dbc.create()

    v2a_db_adapter = ViberToAppDatabaseAdapter(viber_dbc, app_dbc)
    try:
        while True:
            Zlog.info("*"*100)
            Zlog.info(f"Start new lifecycle")
            v2a_db_adapter.translate()
            Zlog.info(f"Sleep {sleep_time}")
            time.sleep(sleep_time)
    finally:
        viber_dbc.disconnect()
        app_dbc.disconnect()
