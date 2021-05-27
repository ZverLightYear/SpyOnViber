from core.adapters.database_adapter import DatabaseAdapter

from core.adapters.viber_to_app.models.viber_to_app_contact_adapter import ViberToAppContactAdapter
from core.adapters.viber_to_app.models.viber_to_app_message_adapter import ViberToAppMessageAdapter
from core.adapters.viber_to_app.models.viber_to_app_chat_adapter import ViberToAppChatAdapter
from core.adapters.viber_to_app.models.viber_to_app_chat_relation_adapter import ViberToAppChatRelationAdapter


class ViberToAppDatabaseAdapter(DatabaseAdapter):
    def __init__(self, viber_db_controller, app_db_controller):
        self.viber_db_controller = viber_db_controller
        self.app_db_controller = app_db_controller

        self.contact_adapter = ViberToAppContactAdapter()
        self.chat_adapter = ViberToAppChatAdapter()
        self.chat_relation_adapter = ViberToAppChatRelationAdapter()
        self.message_adapter = ViberToAppMessageAdapter()

    def connect(self):
        self.viber_db_controller.connect()
        self.app_db_controller.connect()

    def disconnect(self):
        self.viber_db_controller.disconnect()
        self.app_db_controller.disconnect()

    def translate_contact(self):
        self.connect()
        app_last_contact_id = self.app_db_controller.get_last_contact_id()
        viber_contact_list = self.viber_db_controller.get_new_contact_list(app_last_contact_id)
        app_contact_list = self.contact_adapter.translate_list(viber_contact_list)
        self.app_db_controller.insert_contact_list(app_contact_list)
        self.disconnect()

    def translate_chat(self):
        self.connect()
        app_last_chat_id = self.app_db_controller.get_last_chat_id()
        viber_new_chat_list = self.viber_db_controller.get_new_chat_list(app_last_chat_id)
        app_chat_list = self.chat_adapter.translate_list(viber_new_chat_list)
        self.app_db_controller.insert_chat_list(app_chat_list)
        self.disconnect()

    def translate_chat_relation(self):
        self.connect()
        app_last_chat_id = self.app_db_controller.get_last_chat_id()
        app_last_contact_id = self.app_db_controller.get_last_contact_id()
        viber_chat_relation_list = self.viber_db_controller.get_new_chat_relation_list(app_last_chat_id, app_last_contact_id)
        app_chat_relation_list = self.chat_relation_adapter.translate_list(viber_chat_relation_list)
        self.app_db_controller.insert_chat_relation_list(app_chat_relation_list)
        self.disconnect()

    def translate_message(self):
        self.connect()
        app_last_message_id = self.app_db_controller.get_last_message_id()
        viber_message_list = self.viber_db_controller.get_new_message_list_v2(app_last_message_id)
        app_message_list = self.message_adapter.translate_list(viber_message_list)
        self.app_db_controller.insert_message_list(app_message_list)
        self.disconnect()
