class BoatException(Exception):
    """Базовое исключение для лодки"""
    pass


class OverloadException(BoatException):
    """Исключение при перегрузке"""
    pass


class BalanceException(BoatException):
    """Исключение при нарушении баланса"""
    pass


class OarException(BoatException):
    """Исключение для операций с веслами"""
    pass
