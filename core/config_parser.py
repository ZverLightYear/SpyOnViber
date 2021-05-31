import json

from core.zlog.zlog import Zlog


def parse_config(path_to_config=''):
    """
    Парсим файл конфигурации. Возвращаем основные участки конфигурации.
    :param path_to_config: Путь до файла конфигурации относительно вызывающего модуля.
    :return: app_db, viber_db, process_sleep_time.
    """
    conf = json.load(open(rf"{path_to_config}conf.json"))
    Zlog.info("Startup config:")
    Zlog.info(json.dumps(conf, indent=4))

    logging_conf = conf["settings"]["logging"]
    Zlog.logLevel = logging_conf["level"]

    databases_conf = conf["databases"]
    sleep_time = conf["settings"]["process_sleep_time"]

    return databases_conf["app_db"], databases_conf["viber_db"], sleep_time
