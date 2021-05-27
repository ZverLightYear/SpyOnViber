from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class Contact(declarative_base()):
    """
    Модель таблицы Contact БД приложения, содержащая информацию обо всех контактах аккаунта.
    """
    __tablename__ = 'Contact'
    ContactID = Column(Integer, primary_key=True)
    PhoneNumber = Column(String, unique=True)
    Name = Column(String)
    NikName = Column(String)
    DateOfBirth = Column(String)
