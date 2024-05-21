from flask import Flask, request, send_file
from dataclasses import dataclass
from ..Contracts.BaseController import BaseController
from ....Application.usecases import RotateImageUseCase
@dataclass(slots=True, frozen=True)
class ImageRotateController(BaseController):
    use_case: RotateImageUseCase
    def get(self):
        return super().get()
    
    def post(self):
        input_params = RotateImageUseCase.Input(image_path=request.files['image'], angle=request.form.get('angle', 0))
        output = self.use_case.execute(input_params)
        return output