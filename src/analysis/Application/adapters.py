from dataclasses import dataclass
from abc import ABC, abstractmethod
from ..Domain.entities import Analysis

@dataclass(frozen=True, slots=True)
class NpkAnalisysRepository(ABC):
    """
    Abstract base class for NPK analysis repository.
    """
    @abstractmethod
    def add(self, analysis:Analysis):
        raise NotImplementedError("Need to implement add method.")