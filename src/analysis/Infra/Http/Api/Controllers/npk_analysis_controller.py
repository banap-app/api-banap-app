from dataclasses import dataclass
from typing import Any
from ....Adapters.request_adapter import SimpleRequest
from ....Adapters.response_adapter import SimpleResponse
from .....Application.usecases import CreateNpkAnalisys, ListNpkAnalysis


@dataclass(frozen=True, slots=True)
class NpkAnalysisController:
    create_npk_analysis_use_case: CreateNpkAnalisys
    list_npk_analysis_use_case: ListNpkAnalysis

    def create_analysis(self, request: SimpleRequest) -> SimpleResponse:
        """
        Controlador para criar uma nova análise NPK.
        """
        data = request.get_data()
        try:
            # Criando o input para o use case
            input_data = self.create_npk_analysis_use_case.Input(
                phosphor=data["phosphor"],
                potassium=data["potassium"],
                expected_productivity=data["expected_productivity"],
                id_field=data["id_field"]
            )
            
            # Executando o use case
            output = self.create_npk_analysis_use_case.execute(input_data)
            
            # Criando a resposta
            response = SimpleResponse()
            response.set_data({
                "message": output.message,
                "success": output.success,
                "data": {
                    "npk_value": {
                        "id": str(output.npk_value.id),
                        "phosphor": output.npk_value.phosphor,
                        "potassium": output.npk_value.potassium,
                        "expectedProductivity": output.npk_value.expectedProductivity
                    } if output.success else None
                }
            })
            return response
        
        except KeyError as e:
            # Tratando erros de chaves faltando no request
            response = SimpleResponse()
            response.set_data({
                "message": f"Missing field: {str(e)}",
                "success": False
            })
            return response
        
        except Exception as e:
            # Tratando outros erros
            response = SimpleResponse()
            response.set_data({
                "message": f"An error occurred: {str(e)}",
                "success": False
            })
            return response

    def list_analysis(self, request: SimpleRequest) -> SimpleResponse:
        """
        Controlador para listar análises NPK por idField.
        """
        data = request.get_data()
        try:
            # Criando o input para o use case
            input_data = self.list_npk_analysis_use_case.Input(
                idField=data["idField"]
            )
            
            # Executando o use case
            output = self.list_npk_analysis_use_case.execute(input_data)
            
            # Criando a resposta
            response = SimpleResponse()
            response.set_data({
                "message": output.message,
                "success": output.success,
                "data": [
                    {
                        "id": str(analysis.id),
                        "phosphor": analysis.phosphor,
                        "potassium": analysis.potassium,
                        "expectedProductivity": analysis.expectedProductivity
                    } for analysis in output.npk_values
                ] if output.success else []
            })
            return response
        
        except KeyError as e:
            # Tratando erros de chaves faltando no request
            response = SimpleResponse()
            response.set_data({
                "message": f"Missing field: {str(e)}",
                "success": False
            })
            return response
        
        except Exception as e:
            # Tratando outros erros
            response = SimpleResponse()
            response.set_data({
                "message": f"An error occurred: {str(e)}",
                "success": False
            })
            return response
