from core.zlog.zlog import Zlog

from core.adapters.database_adapter import DatabaseAdapter

from core.adapters.viber_to_app.model_adapters.v2a_contact_adapter import V2AContactAdapter
from core.adapters.viber_to_app.model_adapters.v2a_message_adapter import V2AMessageAdapter
from core.adapters.viber_to_app.model_adapters.v2a_chat_adapter import V2AChatAdapter
from core.adapters.viber_to_app.model_adapters.v2a_chat_relation_adapter import V2AChatRelationAdapter


class V2ADatabaseAdapter(DatabaseAdapter):
    def __init__(self, viber_dbc, app_dbc):
        """
        Инициализация транслятора БД Viber в БД приложения.
        :param viber_dbc: контроллер БД Viber.
        :param app_dbc: контроллер БД приложения.
        """
        self.viber_dbc = viber_dbc
        self.app_dbc = app_dbc

        # Задаем трансляторы БД в корректном порядке.
        # Порядок определяется связями моделей.
        self.adapters = [
            V2AContactAdapter(),
            V2AChatAdapter(),
            V2AChatRelationAdapter(),
            V2AMessageAdapter()
        ]

    def translate_all(self):
        """
        Транслировать все модели БД Viber в БД приложения.
        """
        self.connect()

        for model_adapter in self.adapters:
            self.translate_model(model_adapter)

        self.disconnect()

    def connect(self):
        """
        Подключиться к контроллерам БД Viber и приложения.
        """
        self.viber_dbc.connect()
        self.app_dbc.connect()

    def disconnect(self):
        """
        Отключиться от контроллеров БД Viber и приложения.
        """
        self.viber_dbc.disconnect()
        self.app_dbc.disconnect()

    def translate_model(self, model_adapter):
        """
        Транслировать модель БД Viber в модель БД приложения.
        :param model_adapter: транслятор модели БД Viber в модель БД приложения.
        """
        model_from, model_to = model_adapter.models()

        app_model_last_id = self.app_dbc.get_last_model_id(model_to)
        viber_model_new_row_list = self.viber_dbc.get_new_rows(model_from, app_model_last_id)

        Zlog.info(f"New entries to {model_to.__tablename__} model: {len(viber_model_new_row_list)}")

        app_model_new_rows = model_adapter.translate_list(viber_model_new_row_list)
        self.app_dbc.insert_bulk_rows(app_model_new_rows)
