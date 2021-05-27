from __future__ import annotations
from abc import abstractmethod, ABC

from core.adapters.model_adapter import ModelAdapter


class ChatAdapter(ModelAdapter, ABC):
    """
    Интерфейс адаптера чатов.
    Объявляет операции, которые должны выполнять все адаптеры чатов.
    """
