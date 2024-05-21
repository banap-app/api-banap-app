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
        input_params = RotateImageUseCase.Input(**(request.files['image'], request.form.get('angle', 0)))
        self.use_case.execute(input_params)