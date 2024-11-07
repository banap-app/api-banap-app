from flask import Flask, request, jsonify
from typing import Callable
from ....Application.adapters import IRouter
from ...Adapters.request_adapter import SimpleRequest
from ...Adapters.response_adapter import SimpleResponse
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class FlaskRouter(IRouter):
    app: Flask
    
    def add_route(self, path: str, controller_method: Callable, methods=['POST']):
        """
        Registra uma rota no Flask associada a um método do controller.
        """
        self.app.add_url_rule(path, view_func=controller_method, methods=methods)

    def handle_request(self, controller_method: Callable):
        """
        Handle the incoming request, wrapping the request in SimpleRequest and returning SimpleResponse.
        """
        def wrapper():
            try:
                # Pega os dados da requisição do Flask e transforma em SimpleRequest
                request_data = request.json
                
                simple_request = SimpleRequest(data=request_data)
                
                # Chama o método do controller e espera um SimpleResponse
                response: SimpleResponse = controller_method(simple_request)
                
                # Retorna os dados contidos no SimpleResponse
                return jsonify(response.get_data()), 200
            
            except KeyError as e:
                # Tratamento de exceção para campos ausentes
                error_response = SimpleResponse()
                error_response.set_data({
                    "message": f"Missing field: {str(e)}",
                    "success": False
                })
                return jsonify(error_response.get_data()), 400
            
            except Exception as e:
                # Tratamento de exceções genéricas
                error_response = SimpleResponse()
                error_response.set_data({
                    "message": f"An internal error occurred: {str(e)}",
                    "success": False
                })
                return jsonify(error_response.get_data()), 500
        return wrapper
