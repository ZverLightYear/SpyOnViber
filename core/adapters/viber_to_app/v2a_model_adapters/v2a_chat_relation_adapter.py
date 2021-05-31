from core.adapters.model_adapter import ModelAdapter

from core.models.app.chat_relation import ChatRelation as AppChatRelation
from core.models.viber.chat_relation import ChatRelation as ViberChatRelation


class V2AChatRelationAdapter(ModelAdapter):
    """
    Адаптер модели ChatRelation Viber в модель ChatRelation приложения.
    """

    def __init__(self):
        """
        Инициализация адаптера модели ChatRelation Viber в модель ChatRelation приложения.
        """
        pass

    def translate(self, viber_chat_relation: ViberChatRelation):
        """
        Транслирование модели ChatRelation Viber в модель ChatRelation приложения.
        :param viber_chat_relation: модель ChatRelation Viber.
        :return AppChatRelation: модель ChatRelation приложения.
        """
        app_chat_relation = AppChatRelation()
        app_chat_relation.ChatID = viber_chat_relation.ChatID
        app_chat_relation.ContactID = viber_chat_relation.ContactID
        return app_chat_relation

    def model_to(self):
        """
        :return: модель ChatRelation приложения, в которую адаптер производит трансляцию.
        """
        return AppChatRelation

    def model_from(self):
        """
        :return: модель ChatRelation Viber, которую транслирует адаптер.
        """
        return ViberChatRelation
