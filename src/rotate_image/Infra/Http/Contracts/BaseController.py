from abc import ABC
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class BaseController(ABC):
    """
    Base class for all controllers.
    """
    
    def get(self):
        """
        Returns the controller's response.
        """
        raise NotImplementedError()
    def post(self):
        """
        Returns the controller's response.
        """
        raise NotImplementedError()