from flask import Flask, jsonify
from src.analysis.Application.usecases import ListNpkAnalysis, CreateNpkAnalisys
from src.analysis.Infra.Factories.npk_analysis_use_case_factory import NpkAnalysisUseCaseFactory
from src.analysis.Infra.Http.Api.Controllers.npk_analysis_controller import NpkAnalysisController
from src.rotate_image.Infra.Http.Api.ImageRotateController import ImageRotateController
from src.rotate_image.Application.usecases import RotateImageUseCase
from src.rotate_image.Infra.Adapters.RotationImageAdapter import RotationImageAdapter
from src.analysis.Infra.Adapters.request_adapter import SimpleRequest
from src.analysis.Infra.Adapters.response_adapter import SimpleResponse
from src.analysis.Infra.Http.Api.router import FlaskRouter

def create_app():
    """
    Inicializa o app Flask, configura os use cases e adiciona as rotas.
    """
    app = Flask(__name__)

    # Inicialização do factory para NPK Analysis
    npk_usecase_factory = NpkAnalysisUseCaseFactory()

    # Inicialização do FlaskRouter
    router = FlaskRouter(app)

    # Image rotation setup
    rotation_service = RotationImageAdapter()
    rotate_image_usecase = RotateImageUseCase(rotation_service)
    image_rotate_controller = ImageRotateController(rotate_image_usecase)

    # Rotas para análise NPK e rotação de imagens
    @app.route('/send_image', methods=['POST'])
    def send_image():
        output = image_rotate_controller.post()
        return jsonify({'image': output.byte_io_image})

    # Outras rotas relacionadas à NPK Analysis
    def create_npk_analysis_controller_method(request: SimpleRequest) -> SimpleResponse:
        controller = NpkAnalysisController(
            create_npk_analysis_use_case=npk_usecase_factory.create_npk_analisys_usecase(),
            list_npk_analysis_use_case=npk_usecase_factory.list_npk_analisys_usecase()
        )
        return controller.create_analysis(request)

    # Adiciona a rota usando o FlaskRouter
    router.add_route('/create_npk_analysis', router.handle_request(create_npk_analysis_controller_method), methods=['POST'])

    return app
