from core.adapters.model_adapter import ModelAdapter

from core.models.app.chat import Chat as AppChat
from core.models.viber.chat import Chat as ViberChat


class V2AChatAdapter(ModelAdapter):
    """
    Адаптер модели Chat Viber в модель Chat приложения.
    """

    def __init__(self):
        """
        Инициализация адаптера модели Chat Viber в модель Chat приложения.
        """
        pass

    def translate(self, viber_chat: ViberChat):
        """
        Транслирование модели Chat Viber в модель Chat приложения.
        :param viber_chat: модель Chat Viber.
        :return AppChat: модель Chat приложения.
        """
        app_chat = AppChat()
        app_chat.ChatID = viber_chat.ChatID
        app_chat.Name = viber_chat.Name
        app_chat.TabLine = viber_chat.PGTabLine
        app_chat.MetaData = viber_chat.MetaData
        return app_chat

    def model_to(self):
        """
        :return: модель Chat приложения, в которую адаптер производит трансляцию.
        """
        return AppChat

    def model_from(self):
        """
        :return: модель Chat Viber, которую транслирует адаптер.
        """
        return ViberChat
