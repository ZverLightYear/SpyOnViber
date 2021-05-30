from tests.test_v2a.v2a_adapters_suite import TestV2ATranslationSuite

from core.adapters.viber_to_app.v2a_model_adapters.v2a_chat_relation_adapter import V2AChatRelationAdapter
from core.models.viber.chat_relation import ChatRelation as ViberChatRelation
from core.models.app.chat_relation import ChatRelation as AppChatRelation


class TestV2AChatRelationTranslationSuite(TestV2ATranslationSuite):
    def test_model_to(self, **kwargs):
        super().test_model_to(V2AChatRelationAdapter(), AppChatRelation)

    def test_model_from(self, **kwargs):
        super().test_model_from(V2AChatRelationAdapter(), ViberChatRelation)

    def test_models(self, **kwargs):
        super().test_models(V2AChatRelationAdapter(), (ViberChatRelation, AppChatRelation))

    def test_module_translation(self):
        v_chat_relation = ViberChatRelation()

        v_chat_relation.ChatID = 8
        v_chat_relation.ContactID = 9
        v_chat_relation.PGRole = 10

        v2a_chat_relation_adapter = V2AChatRelationAdapter()

        a_chat_relation = v2a_chat_relation_adapter.translate(v_chat_relation)

        assert a_chat_relation.ChatID == v_chat_relation.ChatID
        assert a_chat_relation.ContactID == v_chat_relation.ContactID
