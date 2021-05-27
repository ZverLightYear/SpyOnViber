from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from core.models.app.chat import Chat
from core.models.app.contact import Contact


class Message(declarative_base()):
    """
    Модель таблицы Messages БД приложения, содержащая информацию обо всех сообщениях всех чатов аккаунта.
    """
    __tablename__ = 'Message'
    MessageID = Column(Integer, primary_key=True)
    ChatID = Column(Integer, ForeignKey(Chat.ChatID))
    SenderID = Column(Integer, ForeignKey(Contact.ContactID))
    TimeStamp = Column(String, nullable=False)
    Type = Column(Integer, nullable=False)
    Subject = Column(String(500))
    Body = Column(String(5000))
    PayloadPath = Column(String(1000))
    ThumbnailPath = Column(String(1000))
    MetaData = Column(String)
