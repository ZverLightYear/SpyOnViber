from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class Chat(declarative_base()):
    """
    Модель таблицы Chat БД приложения, содержащая информацию обо всех чатах аккаунта.
    """
    __tablename__ = "Chat"
    ChatID = Column(Integer, primary_key=True)
    Name = Column(String(200))
    TabLine = Column(String)
    MetaData = Column(String)
