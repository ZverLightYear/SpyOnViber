from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from core.models.viber.event import Event


class Message(declarative_base()):
    """
    Модель таблицы Messages БД Viber, содержащая информацию обо всех сообщениях всех чатов аккаунта.
    """
    __tablename__ = 'Messages'
    EventID = Column(Integer, ForeignKey(Event.EventID), primary_key=True, onupdate="CASCADE")
    Type = Column(Integer, nullable=False)
    Status = Column(Integer, nullable=False)
    Subject = Column(String(500))
    Body = Column(String(5000))
    Flag = Column(Integer, default=0)
    PayloadPath = Column(String(1000))
    ThumbnailPath = Column(String(100))
    StickerID = Column(Integer, default=0)
    PttID = Column(String(100))
    PttStatus = Column(Integer, default=0)
    Duration = Column(Integer, default=0)
    PGMessageId = Column(Integer, default=0)
    PGIsLiked = Column(Integer)
    PGLikeCount = Column(Integer)
    Info = Column(String(7000))
    AppId = Column(Integer, default=0)
    ClientFlag = Column(Integer, default=0)
    FollowersLikeCount = Column(Integer, default=0)
