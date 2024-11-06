import sys
import os
from src.analysis.Domain.entities import Analysis
from src.analysis.Application.usecases import ListNpkAnalysis
from src.analysis.Application.adapters import NpkAnalisysRepository
from uuid import UUID, uuid4
from flask import Flask, jsonify
from src.rotate_image.Infra.Http.Api.ImageRotateController import ImageRotateController
from src.rotate_image.Application.usecases import RotateImageUseCase
from src.rotate_image.Infra.Adapters.RotationImageAdapter import RotationImageAdapter

current_script_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_script_path)
sys.path.append(current_directory)

app = Flask(__name__)

class repo(NpkAnalisysRepository):
    def add(self, analysis: Analysis):
        return super().add(analysis)
    
    def listAnalisys(self, idField: UUID):
        return list([idField])    

repot = repo()
use_case = ListNpkAnalysis(npk_analisys_repository=repot)

u = use_case.execute(use_case.Input("9f1454bd-21f7-47a8-a15d-dc648d3e9ad0"))
print(u)
@app.route('/send_image', methods=['POST'])
def send_image():
    rotation_service = RotationImageAdapter()
    usecase = RotateImageUseCase(rotation_service)
    controller = ImageRotateController(usecase)
    output = controller.post()
    return jsonify({'image': output.byte_io_image})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
