import math
from dataclasses import dataclass

from .exceptions import OverloadException, BoatException


@dataclass
class Position:
    x: float
    y: float
    direction: float


class BoatProperties:
    def __init__(self, weight: float, max_load: float, max_oars: int):
        self.weight = weight
        self.max_load = max_load
        self.max_oars = max_oars


class RowingBoat:
    def __init__(self, properties: BoatProperties):
        self.properties = properties
        self.position = Position(x=0.0, y=0.0, direction=0.0)
        self.speed = 0.0
        self.oars = []
        self.in_water = False
        self.passengers = 0
        self.current_load = properties.weight
        self.passenger_weight = 100.0

    def add_passenger(self, weight: float):
        new_total_load = self.current_load + weight
        if new_total_load > self.properties.max_load:
            raise OverloadException("Adding this passenger would exceed the maximum load")
        self.passengers += 1
        self.current_load = new_total_load

    def launch(self):
        if len(self.oars) == 0:
            raise BoatException("Cannot launch without oars")
        self.in_water = True

        self.in_water = True

    def remove_passenger(self, *args):
        if self.passengers <= 0:
            raise BoatException("No passengers to remove")
        self.passengers -= 1
        self.current_load -= self.passenger_weight

    def attach_oar(self, oar):
        if len(self.oars) >= self.properties.max_oars:
            raise BoatException("Maximum number of oars reached")
        self.oars.append(oar)
        return True

    def row(self, strokes):
        if not self.in_water:
            raise BoatException("Boat must be launched before rowing")

        base_speed = 0.5
        oar_efficiency = len(self.oars) * 0.2
        self.speed = base_speed * oar_efficiency * strokes

        self.position.x += self.speed * math.cos(self.position.direction)
        self.position.y += self.speed * math.sin(self.position.direction)

        return self.speed

    def get_position(self):
        return self.position

    def get_load(self):
        return self.current_load
