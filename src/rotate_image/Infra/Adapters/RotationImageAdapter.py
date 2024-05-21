from PIL import Image
from io import BytesIO
from base64 import b64encode
from dataclasses import dataclass
from ...Application.adapters import RotationAdapter

class RotationImageAdapter(RotationAdapter):
    def rotation(self, image_path: str, angle: float):
        image = Image.open(image_path)

    # Rotaciona a imagem
        rotated_image = image.rotate(angle)

    # Salva a imagem rotacionada em um objeto BytesIO
        byte_io = BytesIO()
        rotated_image.save(byte_io, 'JPEG')
        byte_io.seek(0)
        byte_str = b64encode(byte_io.read()).decode('utf-8')
        return byte_str
        
