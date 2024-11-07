
from dataclasses import dataclass
from typing import Any
from ....__seedwork.Infrastructure.Http.response import IResponse

class SimpleResponse(IResponse):
    def __init__(self):
        self._data = None

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data
