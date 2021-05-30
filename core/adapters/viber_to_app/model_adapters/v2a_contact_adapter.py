from core.adapters.model_adapter import ModelAdapter

from core.models.app.contact import Contact as AppContact
from core.models.viber.contact import Contact as ViberContact


class V2AContactAdapter(ModelAdapter):
    def __init__(self):
        pass

    def translate(self, viber_contact: ViberContact):
        app_contact = AppContact()
        app_contact.ContactID = viber_contact.ContactID
        app_contact.Name = viber_contact.Name
        app_contact.NikName = viber_contact.ClientName
        app_contact.DateOfBirth = viber_contact.DateOfBirth
        app_contact.PhoneNumber = viber_contact.Number
        return app_contact

    def model_to(self):
        return AppContact

    def model_from(self):
        return ViberContact
