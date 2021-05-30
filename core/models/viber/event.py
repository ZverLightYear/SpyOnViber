from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from core.models.viber.chat import Chat
from core.models.viber.contact import Contact


class Event(declarative_base()):
    """
    Модель таблицы Events БД Viber, содержащая информацию обо всех событиях всех чатов аккаунта.
    """
    __tablename__ = 'Events'
    EventID = Column(Integer, primary_key=True, autoincrement=True)
    TimeStamp = Column(Integer, nullable=False)
    Direction = Column(Integer, nullable=False)
    Type = Column(Integer, nullable=False)
    ContactLongitude = Column(Integer, default=0)
    ContactLatitude = Column(Integer, default=0)
    ChatID = Column(Integer, ForeignKey(Chat.ChatID), onupdate="CASCADE")
    ContactID = Column(Integer, ForeignKey(Contact.ContactID), onupdate="CASCADE")
    IsSessionLifeTime = Column(Integer, default=0)          # integer(0, 1)
    Flags = Column(Integer, default=0)
    Token = Column(Integer, nullable=False)
    IsRead = Column(Integer, nullable=False, default=0)     # smallint(0, 1)
    SortOrder = Column(Integer, nullable=False, default=0)
    Seq = Column(Integer, nullable=False, default=0)
