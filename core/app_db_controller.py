from core.db_controller import DatabaseController


class ApplicationDatabaseController(DatabaseController):
    """
    Реализация контроллера БД для работы с БД приложения.
    """

    def __init__(self, db_conf):
        """
        Инициализация контроллера БД.
        :param db_conf: конфигурация БД приложения.
        """
        super().__init__(db_conf)
