from ...__seedwork.Domain.entity import Entity
from uuid import UUID, uuid4
from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Analysis(Entity):
    id: Optional[UUID] = uuid4()
    idField: UUID = None
    desiredBaseSaturation: Optional[float] = None
    currentBaseSaturation: Optional[float] = None
    totalCationExchangeCapacity: Optional[float] = None
    relativeTotalNeutralizingPower: Optional[float] = None
    liming: Optional[float] = None
    phosphor: Optional[float] = None
    potassium: Optional[float] = None
    expectedProductivity: Optional[float] = None
    nitrogen: Optional[float] = None
    
    def __post_init__(self):
        self.validate()
    
    def validate(self):
        if not isinstance(self.id, UUID):
            raise ValueError("idField must be an instance of UUID.")
    
    def calculateLiming(self) -> float:
        desired_base_saturation = self.get('desiredBaseSaturation')
        current_base_saturation = self.get('currentBaseSaturation')
        total_cation_exchange_capacity = self.get('totalCationExchangeCapacity')
        relative_total_neutralizing_power = self.get('relativeTotalNeutralizingPower')
        liming = (desired_base_saturation - current_base_saturation) * total_cation_exchange_capacity / relative_total_neutralizing_power
        self.set('liming', liming)
        return round(liming * 100, 1)
    
    def calculate_npk(self):
        if self.expectedProductivity > 50:
            self.set('nitrogen', 410)
            if self.potassium < 1.6:
                self.set('potassium', 800)
            elif 1.6 <= self.potassium <= 3.0:
                self.set('potassium', 950)
            else:
                self.set('potassium', 750)

            if self.phosphor < 16:
                self.set('phosphor', 240)
            elif 16 < self.phosphor <= 40:
                self.set('phosphor', 150)
            else:
                self.set('phosphor', 120)

        elif 40 <= self.expectedProductivity <= 50:
            self.set('nitrogen', 340)
            if self.potassium < 1.6:
                self.set('potassium', 800)
            elif 1.6 <= self.potassium <= 3.0:
                self.set('potassium', 750)
            else:
                self.set('potassium', 550)

            if self.phosphor < 16:
                self.set('phosphor', 220)
            elif 16 < self.phosphor <= 40:
                self.set('phosphor', 130)
            else:
                self.set('phosphor', 110)

        elif 30 <= self.expectedProductivity < 40:
            self.set('nitrogen', 260)
            if self.potassium < 1.6:
                self.set('potassium', 800)
            elif 1.6 <= self.potassium <= 3.0:
                self.set('potassium', 550)
            else:
                self.set('potassium', 350)

            if self.phosphor < 16:
                self.set('phosphor', 200)
            elif 16 < self.phosphor <= 40:
                self.set('phosphor', 110)
            else:
                self.set('phosphor', 80)

        elif 20 <= self.expectedProductivity < 30:
            self.set('nitrogen', 190)
            if self.potassium < 1.6:
                self.set('potassium', 600)
            elif 1.6 <= self.potassium <= 3.0:
                self.set('potassium', 350)
            else:
                self.set('potassium', 150)

            if self.phosphor < 16:
                self.set('phosphor', 180)
            elif 16 < self.phosphor <= 40:
                self.set('phosphor', 90)
            else:
                self.set('phosphor', 60)

        else:
            self.set('nitrogen', 110)
            if self.potassium < 1.6:
                self.set('potassium', 400)
            elif 1.6 <= self.potassium <= 3.0:
                self.set('potassium', 150)
            else:
                self.set('potassium', 100)

            if self.phosphor < 16:
                self.set('phosphor', 160)
            elif 16 < self.phosphor <= 40:
                self.set('phosphor', 70)
            else:
                self.set('phosphor', 40)

    

    
