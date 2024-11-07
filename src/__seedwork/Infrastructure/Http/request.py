from abc import ABC, abstractmethod
from typing import Any
from dataclasses import dataclass


class IRequest(ABC):
    @abstractmethod
    def get_data(self) -> dict:
        """Interface para obter os dados da requisição"""
        pass