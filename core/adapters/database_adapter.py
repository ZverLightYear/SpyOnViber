from __future__ import annotations
from abc import abstractmethod, ABC


class DatabaseAdapter(ABC):
    @abstractmethod
    def translate(self):
        pass
