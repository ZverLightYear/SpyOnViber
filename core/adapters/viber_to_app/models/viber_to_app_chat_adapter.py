from core.adapters.models.chat_adapter import ChatAdapter
from core.models.app.chat import Chat as AppChat


class ViberToAppChatAdapter(ChatAdapter):
    def __init__(self):
        pass

    def translate(self, viber_chat):
        app_chat = AppChat()
        app_chat.ChatID = viber_chat.ChatID
        app_chat.Name = viber_chat.Name
        app_chat.TabLine = viber_chat.PGTabLine
        app_chat.MetaData = viber_chat.MetaData
        return app_chat

