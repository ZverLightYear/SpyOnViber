from core.adapters.model_adapter import ModelAdapter

from core.models.app.chat import Chat as AppChat
from core.models.viber.chat import Chat as ViberChat


class V2AChatAdapter(ModelAdapter):
    def __init__(self):
        pass

    def translate(self, viber_chat: ViberChat):
        app_chat = AppChat()
        app_chat.ChatID = viber_chat.ChatID
        app_chat.Name = viber_chat.Name
        app_chat.TabLine = viber_chat.PGTabLine
        app_chat.MetaData = viber_chat.MetaData
        return app_chat

    def model_to(self):
        return AppChat

    def model_from(self):
        return ViberChat
