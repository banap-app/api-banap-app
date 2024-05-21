import sys, os
from src.rotate_image.Domain.entites import ImageRotate
current_script_path = os.path.realpath(__file__)

# Obtém o diretório do script atual
current_directory = os.path.dirname(current_script_path)
sys.path.append(current_directory)

image = ImageRotate('/teste', 12,12)

print(image.to_dict())

