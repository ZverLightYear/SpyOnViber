from datetime import datetime
from termcolor import colored


class Zlog:
    """
    Логгер сообщений
    """

    logLevel = "NONE"
    tags = {"info": {"tag": " [ * ]", "color": "white"},
            "error": {"tag": " [ ! ]", "color": "red"},
            "debug": {"tag": " [ @ ]", "color": "yellow"},
            "warning": {"tag": " [ ! ]", "color": "yellow"},
            "": {"tag": "      ", "color": "grey"}}

    @staticmethod
    def isDebug():
        """
        Возвращает статус логгера (находится ли он в отладочном режиме или нет)
        :return: статус логгера == DEBUG
        """
        return Zlog.logLevel == "DEBUG"

    @staticmethod
    def log(tag_name, msg, end='\n', without_prefix=False):
        """
        Вывести сообщение.
        :param tag_name: тег сообщения из списка.
        :param msg: сообщение.
        :param end: закончить сообщение специальной строкой. По умолчанию '\n'.
        :param without_prefix: флаг префикса. Если не установлен - время сообщения и тег выводиться не будут.
        """
        if Zlog.isDebug():
            for line in msg.split('\n'):
                color = Zlog.tags[tag_name]["color"]
                if not without_prefix:
                    print(colored(datetime.now().strftime("%H:%M:%S.%f"), color), end='')
                    print(colored(Zlog.tags[tag_name]["tag"], color), end='')
                print(colored(f" {line}", color), end=end)

    @staticmethod
    def info(msg, end='\n', without_prefix=False):
        """
        Вывести информационное сообщение.
        :param msg: сообщение (тег info).
        :param end: закончить сообщение специальной строкой. По умолчанию '\n'.
        :param without_prefix: флаг префикса. Если не установлен - время сообщения и тег выводиться не будут.
        """
        Zlog.log("info", msg, end, without_prefix)

    @staticmethod
    def debug(msg, end='\n', without_prefix=False):
        """
        Вывести отладочное сообщение.
        :param msg: сообщение (тег debug).
        :param end: закончить сообщение специальной строкой. По умолчанию '\n'.
        :param without_prefix: флаг префикса. Если не установлен - время сообщения и тег выводиться не будут.
        """
        Zlog.log("debug", msg, end, without_prefix)

    @staticmethod
    def warning(msg, end='\n', without_prefix=False):
        """
        Вывести предупреждение.
        :param msg: сообщение (тег warning).
        :param end: закончить сообщение специальной строкой. По умолчанию '\n'.
        :param without_prefix: флаг префикса. Если не установлен - время сообщения и тег выводиться не будут.
        """
        Zlog.log("warning", msg, end, without_prefix)

    @staticmethod
    def error(msg, end='\n', without_prefix=False):
        """
        Вывести сообщение об ошибке.
        :param msg: сообщение (тег error).
        :param end: закончить сообщение специальной строкой. По умолчанию '\n'.
        :param without_prefix: флаг префикса. Если не установлен - время сообщения и тег выводиться не будут.
        """
        Zlog.log("error", msg, end, without_prefix)
