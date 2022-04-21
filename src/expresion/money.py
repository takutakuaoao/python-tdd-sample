from expresion.expresion import Expresion


class Money(Expresion):
    _currency: str
    _amount: int

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, "CHF")

    def currency(self) -> str:
        return self._currency

    def __eq__(self, __o: object) -> bool:
        if type(__o) is not Money:
            return False

        return self._amount == __o._amount and self._currency == __o._currency
