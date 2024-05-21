from dataclasses import dataclass
from ...__seedwork.Domain.entity import Entity

@dataclass(frozen=True, slots=True)
class ImageRotate(Entity):
    """
    Rotate an image by a given angle.
    """
    image_path: str
    altura: float
    largura: float
    centro: tuple = None

    def __post_init__(self):
        object.__setattr__(self, 'centro', (self.largura / 2, self.altura / 2))
    



