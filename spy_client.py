import time

from core.config_parser import parse_config
from core.zlog.zlog import Zlog

from core.db_controllers.viber_db_controller import ViberDatabaseController
from core.db_controllers.app_db_controller import ApplicationDatabaseController

from core.adapters.viber_to_app.v2a_adapter import V2AAdapter

if __name__ == '__main__':
    app_db_conf, viber_db_conf, sleep_time = parse_config()

    viber_dbc = ViberDatabaseController(viber_db_conf)
    app_dbc = ApplicationDatabaseController(app_db_conf)

    app_dbc.drop_tables()
    app_dbc.create_tables_with_check()

    v2a_db_adapter = V2AAdapter(viber_dbc, app_dbc)
    try:
        while True:
            Zlog.info("*"*200, without_prefix=True)
            Zlog.info(f"Start new lifecycle")
            v2a_db_adapter.translate_all()
            Zlog.info(f"Sleep {sleep_time}")
            time.sleep(sleep_time)
    finally:
        viber_dbc.disconnect()
        app_dbc.disconnect()
