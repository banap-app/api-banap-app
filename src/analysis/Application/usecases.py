from dataclasses import dataclass
from ...__seedwork.Application.usecase import UseCase
from .adapters import NpkAnalisysRepository
from ..Domain.entities import Analysis

@dataclass(frozen=True, slots=True)
class CreateNpkAnalisys(UseCase):
    npk_analisys_repository:NpkAnalisysRepository
    
    @dataclass(frozen=True, slots=True)
    class Input:
        phosphor: int
        potassium: int
        expected_productivity: int
    
    @dataclass(frozen=True, slots=True)
    class Output:
        npk_value: Analysis
        success: bool
        message: str
    
    
    def execute(self, input_boundary: 'Input'):
        npk_analysis = Analysis(phosphor=input_boundary.phosphor, potassium=input_boundary.potassium, expectedProductivity=input_boundary.expected_productivity)
        try:
            npk_analysis.calculate_npk()
            self.npk_analisys_repository.add(analysis=npk_analysis)
            return self.Output(npk_value=npk_analysis, success=True, message="NPK analysis created successfully")
        except Exception as e:
            return self.Output(npk_value=None, success=False, message=f"Failed to calculate NPK")
        
        
        