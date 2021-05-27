from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from core.models.app.chat import Chat
from core.models.app.contact import Contact

class ChatRelation(declarative_base()):
    """
    Модель таблицы ChatRelation БД приложения, задающая связь между контактами и чатами аккаунта.
    """
    __tablename__ = "ChatRelation"
    RelationID = Column(Integer, primary_key=True, autoincrement=True)
    ChatID = Column(Integer, ForeignKey(Chat.ChatID), nullable=False, primary_key=True)
    ContactID = Column(Integer, ForeignKey(Contact.ContactID), nullable=False, primary_key=True)
