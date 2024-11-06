from dataclasses import dataclass
from abc import ABC, abstractmethod
from uuid import UUID
from ..Domain.entities import Analysis

@dataclass(frozen=True, slots=True)
class NpkAnalisysRepository(ABC):
    """
    Abstract base class for NPK analysis repository.
    """
    @abstractmethod
    def add(self, analysis:Analysis):
        raise NotImplementedError("Need to implement add method.")
    
    def listAnalisys(self, idField: UUID):
        """
        Returns all NPK analyses based on the provided idField.
        """
        raise NotImplementedError("Need to implement listAnalisys method.")