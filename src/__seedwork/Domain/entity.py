from abc import ABC
from dataclasses import asdict, dataclass

@dataclass(frozen=True, slots=True)
class Entity(ABC):
    
    def to_dict(self):
        return asdict(self)