from datetime import datetime
from termcolor import colored


class Zlog:
    logLevel = "NONE"

    tags = {"info": {"tag": " [ * ]", "color": "white"},
            "error": {"tag": " [ ! ]", "color": "red"},
            "abort": {"tag": " [ X ]", "color": "red"},
            "debug": {"tag": " [ @ ]", "color": "yellow"},
            "warning": {"tag": " [ ! ]", "color": "yellow"},
            "": {"tag": "      ", "color": "grey"}}

    Types = []

    @staticmethod
    def isDebug():
        return Zlog.logLevel == "DEBUG"

    @staticmethod
    def log(tag_name, msg, end='\n', without_prefix=False):
        if Zlog.isDebug():
            for line in msg.split('\n'):
                color = Zlog.tags[tag_name]["color"]
                if not without_prefix:
                    print(colored(datetime.now().strftime("%H:%M:%S.%f"), color), end='')
                    print(colored(Zlog.tags[tag_name]["tag"], color), end='')
                print(colored(f" {line}", color), end=end)

    @staticmethod
    def message(msg, end='\n', without_prefix=False):
        Zlog.log("", msg, end, without_prefix)

    @staticmethod
    def info(msg, end='\n', without_prefix=False):
        Zlog.log("info", msg, end, without_prefix)

    @staticmethod
    def debug(msg, end='\n', without_prefix=False):
        Zlog.log("debug", msg, end, without_prefix)

    @staticmethod
    def warning(msg, end='\n', without_prefix=False):
        Zlog.log("warning", msg, end, without_prefix)

    @staticmethod
    def error(msg, end='\n', without_prefix=False):
        Zlog.log("error", msg, end, without_prefix)

    @staticmethod
    def abort(msg, end='\n', without_prefix=False):
        Zlog.log("abort", msg, end, without_prefix)
