from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class Chat(declarative_base()):
    """
    Модель таблицы Chat БД Viber, содержащая информацию обо всех чатах аккаунта.
    """
    __tablename__ = "ChatInfo"
    ChatID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(200))
    Token = Column(String(50), unique=True)
    Flags = Column(Integer, default=0)
    TimeStamp = Column(Integer, nullable=False)
    IconID = Column(String(255))
    BackgroundID = Column(String(255))
    LastReadMessageToken = Column(Integer, default=0)
    LastReadMessageId = Column(Integer, default=0)
    LastSeenMessageToken = Column(Integer, default=0)
    PGType = Column(Integer)
    PGUri = Column(String(255))
    PGRevision = Column(Integer)
    PGLongtitude = Column(Integer)
    PGLatitude = Column(Integer)
    PGCountry = Column(String(255))
    PGTabLine = Column(String(255))
    PGTags = Column(String(255))
    PGLastMessageID = Column(Integer)
    PGWatchersCount = Column(Integer)
    PGSearchFlags = Column(Integer)
    MetaData = Column(String(255))
