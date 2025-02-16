from dataclasses import dataclass
from enum import Enum


class OarState(Enum):
    IN_WATER = "in_water"
    ABOVE_WATER = "above_water"
    STORED = "stored"


@dataclass
class OarPosition:
    angle: float  # угол относительно поверхности воды
    depth: float  # глубина погружения в воду


class Oar:
    def __init__(self, length: float, blade_area: float):
        self.length = length
        self.blade_area = blade_area
        self.state = OarState.STORED
        self.position = OarPosition(angle=0.0, depth=0.0)
        self.is_attached = False

    def get_state(self) -> OarState:
        """Получить текущее состояние весла"""
        return self.state

    def set_state(self, state: OarState) -> None:
        """Установить состояние весла"""
        self.state = state
