from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class Contact(declarative_base()):
    """
    Модель таблицы Contact БД приложения, содержащая информацию обо всех контактах аккаунта.
    """
    __tablename__ = 'Contact'
    ContactID = Column(Integer, index=True, primary_key=True)
    PhoneNumber = Column(String, index=True, unique=True)
    Name = Column(String)
    NikName = Column(String)
    DateOfBirth = Column(String)
