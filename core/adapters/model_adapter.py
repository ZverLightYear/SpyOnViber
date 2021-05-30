from __future__ import annotations
from abc import abstractmethod, ABC


class ModelAdapter(ABC):
    """
    Интерфейс адаптера моделй.
    Объявляет операции, которые должны выполнять все адаптеры моделей.
    """
    @abstractmethod
    def __init__(self):
        """
        Инициализация адаптера моделей.
        """
        pass

    @abstractmethod
    def model_to(self):
        pass

    @abstractmethod
    def model_from(self):
        pass

    def models(self):
        return self.model_from(), self.model_to()

    @abstractmethod
    def translate(self, in_arg):
        """
        Трансляция модели.
        :param in_arg: модель.
        :return: транслированная модель.
        """
        pass

    def translate_list(self, in_args_list):
        """
        Трансляция списка моделей.
        :param in_args_list: список моделей.
        :return: список транслированных моделей.
        """
        return map(self.translate, in_args_list)
