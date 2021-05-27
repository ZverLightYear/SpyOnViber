from __future__ import annotations
from abc import abstractmethod, ABC

from core.adapters.model_adapter import ModelAdapter


class ContactAdapter(ModelAdapter, ABC):
    """
    Интерфейс адаптера контактов.
    Объявляет операции, которые должны выполнять все адаптеры контактов.
    """
