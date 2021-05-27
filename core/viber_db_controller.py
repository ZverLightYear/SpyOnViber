from core.db_controller import DatabaseController


class ViberDatabaseController(DatabaseController):
    """
    Реализация контроллера БД для работы с БД Viber.
    """
    def __init__(self, db_conf):
        """
        Инициализация контроллера БД.
        :param db_conf: конфигурация БД Viber.
        """
        super().__init__(db_conf)
