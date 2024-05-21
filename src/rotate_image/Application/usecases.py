from dataclasses import dataclass
from io import BytesIO
from .adapters import RotationAdapter
from ..Domain.entites import ImageRotate
from ...__seedwork.Application.usecase import UseCase


@dataclass(frozen=True, slots=True)
class RotateImageUseCase(UseCase):
    rotatation_adapter: RotationAdapter
    
    @dataclass(frozen=True, slots=True)
    class Input:
        image_path: str
        angle: float
    
    @dataclass(frozen=True, slots=True)
    class Output:
        byte_io_image: BytesIO
    
    def execute(self, input_boundary: 'Input'):
        image_for_rotate = ImageRotate(input_boundary.image_path, 0, 0)
        output = self.rotatation_adapter.rotation(input_boundary.image_path, float(input_boundary.angle))
        return self.Output(byte_io_image=output)