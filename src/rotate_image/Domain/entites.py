from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ImageRotate():
    """
    Rotate an image by a given angle.
    """
    image_path: str
    altura: float
    largura: float
    centro: tuple = None

    def __post_init__(self):
        object.__setattr__(self, 'centro', (self.largura / 2, self.altura / 2))
    
    

image = ImageRotate('a', 12,12)


