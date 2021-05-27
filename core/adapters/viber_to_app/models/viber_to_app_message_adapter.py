from core.adapters.models.message_adapter import MessageAdapter
from core.models.app.message import Message as AppMessage


class ViberToAppMessageAdapter(MessageAdapter):
    def __init__(self):
        pass

    def translate(self, viber_message_join_event):
        viber_message, viber_event = viber_message_join_event
        app_message = AppMessage()
        app_message.MessageID = viber_message.EventID
        app_message.ChatID = viber_event.ChatID
        app_message.SenderID = viber_event.ContactID
        app_message.TimeStamp = viber_event.TimeStamp
        app_message.Type = viber_message.Type
        app_message.Subject = viber_message.Subject
        app_message.Body = viber_message.Body
        app_message.PayloadPath = viber_message.PayloadPath
        app_message.ThumbnailPath = viber_message.ThumbnailPath
        app_message.MetaData = viber_message.Info
        return app_message
