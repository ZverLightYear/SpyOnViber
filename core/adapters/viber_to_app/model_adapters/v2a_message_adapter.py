from core.adapters.model_adapter import ModelAdapter

from core.models.app.message import Message as AppMessage
from core.models.viber.message import Message as ViberMessage


class V2AMessageAdapter(ModelAdapter):
    def __init__(self):
        """
        Инициализация адаптера модели Message Viber в модель Message приложения.
        """
        pass

    def translate(self, viber_message_join_event: ViberMessage):
        """
        Транслирование модели Message Viber в модель Message приложения.
        """
        app_message = AppMessage()
        app_message.MessageID = viber_message_join_event.EventID
        app_message.ChatID = viber_message_join_event.ChatID
        app_message.SenderID = viber_message_join_event.ContactID
        app_message.TimeStamp = viber_message_join_event.TimeStamp
        app_message.Type = viber_message_join_event.Type
        app_message.Subject = viber_message_join_event.Subject
        app_message.Body = viber_message_join_event.Body
        app_message.PayloadPath = viber_message_join_event.PayloadPath
        app_message.ThumbnailPath = viber_message_join_event.ThumbnailPath
        app_message.MetaData = viber_message_join_event.Info
        return app_message

    def model_to(self):
        """
        :return: модель Message приложения, в которую адаптер производит трансляцию.
        """
        return AppMessage

    def model_from(self):
        """
        :return: модель Message Viber, которую транслирует адаптер.
        """
        return ViberMessage
