from core.adapters.database_adapter import DatabaseAdapter

from core.adapters.viber_to_app.models.viber_to_app_contact_adapter import ViberToAppContactAdapter
from core.adapters.viber_to_app.models.viber_to_app_message_adapter import ViberToAppMessageAdapter
from core.adapters.viber_to_app.models.viber_to_app_chat_adapter import ViberToAppChatAdapter
from core.adapters.viber_to_app.models.viber_to_app_chat_relation_adapter import ViberToAppChatRelationAdapter


class ViberToAppDatabaseAdapter(DatabaseAdapter):
    def __init__(self, viber_database_controller, app_database_controller):
        self.viber_database_controller = viber_database_controller
        self.app_database_controller = app_database_controller

        self.contact_adapter = ViberToAppContactAdapter()
        self.chat_adapter = ViberToAppChatAdapter()
        self.chat_relation_adapter = ViberToAppChatRelationAdapter()
        self.message_adapter = ViberToAppMessageAdapter()

    def connect(self):
        self.viber_database_controller.connect()
        self.app_database_controller.connect()

    def disconnect(self):
        self.viber_database_controller.disconnect()
        self.app_database_controller.disconnect()

    def translate_contact(self):
        self.connect()
        viber_contact_list = self.viber_database_controller.get_contact_list()
        app_contact_list = self.contact_adapter.translate_list(viber_contact_list)
        self.app_database_controller.insert_contact_list(app_contact_list)
        self.disconnect()

    def translate_chat(self):
        self.connect()
        viber_chat_list = self.viber_database_controller.get_chat_list()
        app_chat_list = self.chat_adapter.translate_list(viber_chat_list)
        self.app_database_controller.insert_chat_list(app_chat_list)
        self.disconnect()

    def translate_chat_relation(self):
        self.connect()
        viber_chat_relation_list = self.viber_database_controller.get_chat_relation_list()
        app_chat_relation_list = self.chat_relation_adapter.translate_list(viber_chat_relation_list)
        self.app_database_controller.insert_chat_relation_list(app_chat_relation_list)
        self.disconnect()

    def translate_message(self):
        self.connect()
        viber_message_list = self.viber_database_controller.get_message_list_v2()
        app_message_list = self.message_adapter.translate_list(viber_message_list)
        self.app_database_controller.insert_message_list(app_message_list)
        self.disconnect()
