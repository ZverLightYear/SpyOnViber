from __future__ import annotations
from abc import abstractmethod, ABC


class DatabaseAdapter(ABC):
    @abstractmethod
    def translate_all(self):
        """
        Транслировать все модели БД.
        """
        pass
