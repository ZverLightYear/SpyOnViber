from core.adapters.model_adapter import ModelAdapter

from core.models.app.chat_relation import ChatRelation as AppChatRelation
from core.models.viber.chat_relation import ChatRelation as ViberChatRelation


class V2AChatRelationAdapter(ModelAdapter):
    def __init__(self):
        pass

    def translate(self, viber_chat_relation: ViberChatRelation):
        app_chat_relation = AppChatRelation()
        app_chat_relation.ChatID = viber_chat_relation.ChatID
        app_chat_relation.ContactID = viber_chat_relation.ContactID
        return app_chat_relation

    def model_to(self):
        return AppChatRelation

    def model_from(self):
        return ViberChatRelation
