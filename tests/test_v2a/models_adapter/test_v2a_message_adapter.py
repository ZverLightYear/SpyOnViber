from sqlalchemy.engine import LegacyRow
from sqlalchemy.orm import join

from tests.test_v2a.v2a_adapters_suite import TestV2ATranslationSuite

from core.adapters.viber_to_app.v2a_model_adapters.v2a_message_adapter import V2AMessageAdapter
from core.models.viber.message import Message as ViberMessage
from core.models.viber.event import Event as ViberEvent
from core.models.app.message import Message as AppMessage


class TestV2AContactTranslationSuite(TestV2ATranslationSuite):
    def test_model_to(self, **kwargs):
        super().test_model_to(V2AMessageAdapter(), AppMessage)

    def test_model_from(self, **kwargs):
        super().test_model_from(V2AMessageAdapter(), ViberMessage)

    def test_models(self, **kwargs):
        super().test_models(V2AMessageAdapter(), (ViberMessage, AppMessage))

    def test_module_translation(self):
        v_message_join_event = join(ViberMessage, ViberEvent, ViberMessage.EventID == ViberEvent.EventID)

        v_message_join_event.EventID = 15
        v_message_join_event.ChatID = 16
        v_message_join_event.ContactID = 17
        v_message_join_event.TimeStamp = 123456789
        v_message_join_event.Type = 18
        v_message_join_event.Subject = "Subject"
        v_message_join_event.Body = "Body"
        v_message_join_event.PayloadPath = "PayloadPath"
        v_message_join_event.ThumbnailPath = "ThumbnailPath"
        v_message_join_event.Info = "Info"

        v2a_message_adapter = V2AMessageAdapter()
        a_message = v2a_message_adapter.translate(v_message_join_event)

        assert a_message.MessageID == v_message_join_event.EventID
        assert a_message.ChatID == v_message_join_event.ChatID
        assert a_message.SenderID == v_message_join_event.ContactID
        assert a_message.TimeStamp == v_message_join_event.TimeStamp
        assert a_message.Type == v_message_join_event.Type
        assert a_message.Subject == v_message_join_event.Subject
        assert a_message.Body == v_message_join_event.Body
        assert a_message.PayloadPath == v_message_join_event.PayloadPath
        assert a_message.ThumbnailPath == v_message_join_event.ThumbnailPath
        assert a_message.MetaData == v_message_join_event.Info
