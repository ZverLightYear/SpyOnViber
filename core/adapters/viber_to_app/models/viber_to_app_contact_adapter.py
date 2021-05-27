from core.adapters.models.contact_adapter import ContactAdapter
from core.models.app.contact import Contact as AppContact


class ViberToAppContactAdapter(ContactAdapter):
    def __init__(self):
        pass

    def translate(self, viber_contact):
        app_contact = AppContact()
        app_contact.ContactID = viber_contact.ContactID
        app_contact.Name = viber_contact.Name
        app_contact.NikName = viber_contact.ClientName
        app_contact.DateOfBirth = viber_contact.DateOfBirth
        app_contact.PhoneNumber = viber_contact.Number
        return app_contact
