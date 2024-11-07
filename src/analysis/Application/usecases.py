from dataclasses import dataclass
from uuid import UUID
from ...__seedwork.Application.usecase import UseCase
from .adapters import NpkAnalisysRepository
from ..Domain.entities import Analysis


@dataclass(frozen=True, slots=True)
class CreateNpkAnalisys(UseCase):
    npk_analisys_repository: NpkAnalisysRepository

    @dataclass(frozen=True, slots=True)
    class Input:
        phosphor: int
        potassium: int
        expected_productivity: int
        id_field: UUID

    @dataclass(frozen=True, slots=True)
    class Output:
        npk_value: Analysis
        success: bool
        message: str

    def execute(self, input_boundary: 'Input'):
        npk_analysis = Analysis(idField=input_boundary.id_field,phosphor=input_boundary.phosphor, potassium=input_boundary.potassium,
                                expectedProductivity=input_boundary.expected_productivity)
        try:
            npk_analysis.calculate_npk()
            print(npk_analysis.to_dict())
            self.npk_analisys_repository.add(analysis=npk_analysis)
            return self.Output(npk_value=npk_analysis, success=True, message="NPK analysis created successfully")
        except Exception as e:
            return self.Output(npk_value=None, success=False, message=f"Failed to calculate NPK")


@dataclass(frozen=True, slots=True)
class ListNpkAnalysis(UseCase):
    npk_analisys_repository: NpkAnalisysRepository

    @dataclass(frozen=True, slots=True)
    class Output:
        npk_values: list[Analysis]
        success: bool
        message: str

    @dataclass(frozen=True, slots=True)
    class Input:
        idField: str

    def execute(self, input_boundary: 'Input'):
        uuid_valid = UUID(input_boundary.idField)
        try:
            analisys: list[Analysis] = self.npk_analisys_repository.listAnalisys(uuid_valid)
            return self.Output(npk_values=analisys, success=True, message="NPK analysis found successfully")
        except Exception as e:
            return self.Output(npk_values=[], success=False, message=f"Failed to find NPK analysis {e}")
