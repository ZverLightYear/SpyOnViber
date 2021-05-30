from tests.test_v2a.v2a_adapters_suite import TestV2ATranslationSuite

from core.adapters.viber_to_app.v2a_model_adapters.v2a_contact_adapter import V2AContactAdapter
from core.models.viber.contact import Contact as ViberContact
from core.models.app.contact import Contact as AppContact


class TestV2AContactTranslationSuite(TestV2ATranslationSuite):
    def test_model_to(self, **kwargs):
        super().test_model_to(V2AContactAdapter(), AppContact)

    def test_model_from(self, **kwargs):
        super().test_model_from(V2AContactAdapter(), ViberContact)

    def test_models(self, **kwargs):
        super().test_models(V2AContactAdapter(), (ViberContact, AppContact))

    def test_module_translation(self):
        v_contact = ViberContact()

        v_contact.ContactID = 15
        v_contact.Name = "Name"
        v_contact.ABContact = 10
        v_contact.ViberContact = 20
        v_contact.Number = "Number"
        v_contact.MID = "MID"
        v_contact.EncryptedNumber = "EncryptedNumber"
        v_contact.EncryptedMID = "EncryptedMID"
        v_contact.VID = "VID"
        v_contact.ClientName = "ClientName"
        v_contact.DownloadID = "DownloadID"
        v_contact.ContactFlags = 30
        v_contact.SortName = "SortName"
        v_contact.Timestamp = 123456789
        v_contact.DateOfBirth = "DateOfBirth"

        v2a_contact_adapter = V2AContactAdapter()

        a_contact = v2a_contact_adapter.translate(v_contact)

        assert a_contact.ContactID == v_contact.ContactID
        assert a_contact.Name == v_contact.Name
        assert a_contact.DateOfBirth == v_contact.DateOfBirth
        assert a_contact.NikName == v_contact.ClientName
        assert a_contact.PhoneNumber == v_contact.Number
