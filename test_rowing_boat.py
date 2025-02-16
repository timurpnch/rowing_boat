import pytest

from .src.exceptions import OverloadException, BoatException
from .src.oar import Oar, OarState


# Системное тестирование

def test_boat_floating_empty(boat):
    """Проверка запуска пустой лодки"""
    with pytest.raises(BoatException, match="Cannot launch without oars"):
        boat.launch()


def test_maximum_load_capacity(boat):
    """Проверка максимальной нагрузки"""

    # Сначала добавляем пассажира с допустимым весом
    boat.add_passenger(100.0)  # Текущая нагрузка: 200 (лодка) + 100 = 300

    # Пытаемся добавить пассажира, который превысит максимальную нагрузку
    with pytest.raises(OverloadException):
        boat.add_passenger(300.0)  # Попытка добавить: 300 + 300 = 600 > max_load (500)


# Интеграционное тестирование

def test_oar_attachment(boat):
    """Проверка прикрепления весел"""
    oar = Oar(length=2.0, blade_area=0.1)
    assert boat.attach_oar(oar)


def test_rowing_mechanics(boat):
    """Проверка механики гребли"""
    oar = Oar(length=2.0, blade_area=0.1)
    boat.attach_oar(oar)
    boat.launch()
    speed = boat.row(5)  # 5 гребков
    assert speed > 0.001


# Функциональное тестирование

def test_oar_states(oar):
    """ Проверка состояний вёсел"""

    # Проверяем начальное состояние
    assert oar.get_state() == OarState.STORED

    # Меняем состояние весла
    oar.set_state(OarState.IN_WATER)
    assert oar.get_state() == OarState.IN_WATER

    oar.set_state(OarState.ABOVE_WATER)
    assert oar.get_state() == OarState.ABOVE_WATER

    # Проверяем параметры весла
    assert oar.length > 0
    assert oar.blade_area > 0


def test_boat_movement_restrictions(boat):
    """Проверка ограничений движения"""
    oar = Oar(length=2.0, blade_area=0.1)
    boat.attach_oar(oar)
    boat.launch()
    speed = boat.row(3)
    assert speed > 0


def test_passenger_management(boat):
    """Управление пассажирами"""
    boat.add_passenger(100.0)  # используем точный вес
    assert boat.get_load() == boat.properties.weight + 100.0
