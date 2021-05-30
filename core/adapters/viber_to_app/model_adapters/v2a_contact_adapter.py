from core.adapters.model_adapter import ModelAdapter

from core.models.app.contact import Contact as AppContact
from core.models.viber.contact import Contact as ViberContact


class V2AContactAdapter(ModelAdapter):
    def __init__(self):
        """
        Инициализация адаптера модели Contact Viber в модель Contact приложения.
        """
        pass

    def translate(self, viber_contact: ViberContact):
        """
        Транслирование модели Contact Viber в модель Contact приложения.
        """
        app_contact = AppContact()
        app_contact.ContactID = viber_contact.ContactID
        app_contact.Name = viber_contact.Name
        app_contact.NikName = viber_contact.ClientName
        app_contact.DateOfBirth = viber_contact.DateOfBirth
        app_contact.PhoneNumber = viber_contact.Number
        return app_contact

    def model_to(self):
        """
        :return: модель Contact приложения, в которую адаптер производит трансляцию.
        """
        return AppContact

    def model_from(self):
        """
        :return: модель Contact Viber, которую транслирует адаптер.
        """
        return ViberContact
