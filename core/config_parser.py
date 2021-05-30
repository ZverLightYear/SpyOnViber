import json

from core.zlog.zlog import Zlog


def parse_config(path_to_config=''):
    conf = json.load(open(rf"{path_to_config}conf.json"))

    logging_conf = conf["settings"]["logging"]
    Zlog.logLevel = logging_conf["level"]

    databases_conf = conf["databases"]
    Zlog.info("Startup config:")
    Zlog.info(json.dumps(databases_conf, indent=4))

    sleep_time = conf["settings"]["process_sleep_time"]

    return databases_conf["app_db"], databases_conf["viber_db"], sleep_time
