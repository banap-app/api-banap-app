from dataclasses import dataclass
from abc import ABC, abstractmethod
from io import BytesIO

@dataclass(frozen=True, slots=True)
class RotationAdapter(ABC):
    """
    Abstract base class for rotation adapters.
    """
    @abstractmethod
    def rotation(self, image_path:str, angle:float)-> BytesIO:
        raise NotImplementedError("Need to implement rotation method.")