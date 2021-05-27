from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class Contact(declarative_base()):
    """
    Модель таблицы Contact БД Viber, содержащая информацию обо всех контактах аккаунта.
    """
    __tablename__ = 'Contact'
    ContactID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    ABContact = Column(Integer, nullable=False, default=0)
    ViberContact = Column(Integer, nullable=False, default=0)
    Number = Column(String, unique=True)
    MID = Column(String, unique=True)
    EncryptedNumber = Column(String, unique=True)
    EncryptedMID = Column(String, unique=True)
    VID = Column(String, unique=True)
    ClientName = Column(String)
    DownloadID = Column(String)
    ContactFlags = Column(Integer, default=0)
    SortName = Column(String)
    Timestamp = Column(Integer, default=0)
    DateOfBirth = Column(String)
