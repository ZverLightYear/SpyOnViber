from __future__ import annotations
from abc import abstractmethod, ABC

from core.adapters.model_adapter import ModelAdapter


class ChatRelationsAdapter(ModelAdapter, ABC):
    """
    Интерфейс адаптера связей между контактами и чатами.
    Объявляет операции, которые должны выполнять все адаптеры связей между контактами и чатами.
    """
