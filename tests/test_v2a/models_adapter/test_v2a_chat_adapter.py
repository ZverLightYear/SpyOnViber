from tests.test_v2a.v2a_adapters_suite import TestV2ATranslationSuite

from core.adapters.viber_to_app.v2a_model_adapters.v2a_chat_adapter import V2AChatAdapter
from core.models.viber.chat import Chat as ViberChat
from core.models.app.chat import Chat as AppChat


class TestV2AChatTranslationSuite(TestV2ATranslationSuite):
    def test_model_to(self, **kwargs):
        super().test_model_to(V2AChatAdapter(), AppChat)

    def test_model_from(self, **kwargs):
        super().test_model_from(V2AChatAdapter(), ViberChat)

    def test_models(self, **kwargs):
        super().test_models(V2AChatAdapter(), (ViberChat, AppChat))

    def test_module_translation(self):
        v_chat = ViberChat()
        v_chat.ChatID = 15
        v_chat.Name = "Name"
        v_chat.Token = "Token"
        v_chat.Token = "Token"
        v_chat.Flags = 128
        v_chat.TimeStamp = 1234567890
        v_chat.IconID = "IconID"
        v_chat.BackgroundID = "BackgroundID"
        v_chat.LastReadMessageToken = 100
        v_chat.LastReadMessageId = 90
        v_chat.LastSeenMessageToken = 80
        v_chat.PGType = 70
        v_chat.PGUri = "PGUri"
        v_chat.PGRevision = 60
        v_chat.PGLongtitude = 50
        v_chat.PGLatitude = 40
        v_chat.PGCountry = "PGCountry"
        v_chat.PGTabLine = "PGTabLine"
        v_chat.PGTags = "PGTags"
        v_chat.PGLastMessageID = 30
        v_chat.PGWatchersCount = 20
        v_chat.PGSearchFlags = 10
        v_chat.MetaData = "MetaData"

        v2a_chat_adapter = V2AChatAdapter()

        a_chat = v2a_chat_adapter.translate(v_chat)

        assert a_chat.ChatID == v_chat.ChatID
        assert a_chat.Name == v_chat.Name
        assert a_chat.MetaData == v_chat.MetaData
        assert a_chat.TabLine == v_chat.PGTabLine
