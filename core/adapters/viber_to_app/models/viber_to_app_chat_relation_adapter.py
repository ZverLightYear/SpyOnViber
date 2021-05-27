from core.adapters.models.chat_relation_adapter import ChatRelationsAdapter
from core.models.app.chat_relation import ChatRelation as AppChatRelation


class ViberToAppChatRelationAdapter(ChatRelationsAdapter):
    def __init__(self):
        pass

    def translate(self, viber_chat_relation):
        app_chat_relation = AppChatRelation()
        app_chat_relation.ChatID = viber_chat_relation.ChatID
        app_chat_relation.ContactID = viber_chat_relation.ContactID
        return app_chat_relation
