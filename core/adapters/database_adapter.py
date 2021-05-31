from __future__ import annotations
from abc import abstractmethod, ABC


class DatabaseAdapter(ABC):
    """
    Адаптер БД Viber в БД приложения.
    """

    @abstractmethod
    def translate_all(self):
        """
        Транслировать все модели БД.
        """
        pass
