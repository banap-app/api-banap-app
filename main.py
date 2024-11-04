import sys
import os
from src.analysis.Domain.entities import Analysis
from src.analysis.Application.usecases import CreateNpkAnalisys
from src.analysis.Application.adapters import NpkAnalisysRepository
from uuid import uuid4
from flask import Flask, jsonify
from src.rotate_image.Infra.Http.Api.ImageRotateController import ImageRotateController
from src.rotate_image.Application.usecases import RotateImageUseCase
from src.rotate_image.Infra.Adapters.RotationImageAdapter import RotationImageAdapter

current_script_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_script_path)
sys.path.append(current_directory)

app = Flask(__name__)

@app.route('/send_image', methods=['POST'])
def send_image():
    rotation_service = RotationImageAdapter()
    usecase = RotateImageUseCase(rotation_service)
    controller = ImageRotateController(usecase)
    output = controller.post()
    return jsonify({'image': output.byte_io_image})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
