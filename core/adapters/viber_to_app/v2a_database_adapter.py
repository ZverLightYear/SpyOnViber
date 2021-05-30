from core.zlog.zlog import Zlog

from sqlalchemy.inspection import inspect

from core.adapters.database_adapter import DatabaseAdapter

from core.adapters.viber_to_app.model_adapters.v2a_contact_adapter import V2AContactAdapter
from core.adapters.viber_to_app.model_adapters.v2a_message_adapter import V2AMessageAdapter
from core.adapters.viber_to_app.model_adapters.v2a_chat_adapter import V2AChatAdapter
from core.adapters.viber_to_app.model_adapters.v2a_chat_relation_adapter import V2AChatRelationAdapter


class V2ADatabaseAdapter(DatabaseAdapter):
    def __init__(self, viber_dbc, app_dbc):
        self.viber_dbc = viber_dbc
        self.app_dbc = app_dbc

        self.adapters = [
            V2AContactAdapter(),
            V2AChatAdapter(),
            V2AChatRelationAdapter(),
            V2AMessageAdapter()
        ]

    def connect(self):
        self.viber_dbc.connect()
        self.app_dbc.connect()

    def disconnect(self):
        self.viber_dbc.disconnect()
        self.app_dbc.disconnect()

    def translate_all(self):
        self.connect()

        for model_adapter in self.adapters:
            self.translate_model(model_adapter)

        self.disconnect()

    def translate_model(self, model_adapter):
        model_from, model_to = model_adapter.models()

        model_to_primary_keys = inspect(model_to).primary_key
        model_from_primary_keys = inspect(model_from).primary_key

        app_last_model_id = list(map(self.app_dbc.get_last_model_id, model_to_primary_keys))
        viber_new_model_list = self.viber_dbc.get_new_rows(model_from, model_from_primary_keys, app_last_model_id)

        Zlog.info(f"New entries to {model_to.__tablename__} model: {len(viber_new_model_list)}")

        app_model_list = model_adapter.translate_list(viber_new_model_list)
        self.app_dbc.insert_bulk_rows(app_model_list)
