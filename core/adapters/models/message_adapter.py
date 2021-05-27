from __future__ import annotations
from abc import abstractmethod, ABC

from core.adapters.model_adapter import ModelAdapter


class MessageAdapter(ModelAdapter, ABC):
    """
    Интерфейс адаптера сообщений.
    Объявляет операции, которые должны выполнять все адаптеры сообщений.
    """
