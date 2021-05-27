from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class ChatRelation(declarative_base()):
    """
    Модель таблицы ChatRelation БД Viber, задающая связь между контактами и чатами аккаунта.
    """
    __tablename__ = "ChatRelation"
    ChatID = Column(Integer, ForeignKey('ChatInfo.ChatID'), nullable=False, primary_key=True)
    ContactID = Column(Integer, ForeignKey('Contact.ContactID'), nullable=False, primary_key=True)
    PGRole = Column(Integer)
