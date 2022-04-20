class Money:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        return Dollar(amount)

    def __eq__(self, __o: 'Money') -> bool:
        if isinstance(__o, Money) == False:
            return False

        return self._amount == __o._amount and type(self) == type(__o)

class Dollar(Money):
    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int) -> 'Money':
        return Dollar(self._amount * multiplier)

class Franc(Money):
    def __init__(self, amount:int):
        super().__init__(amount)

    def times(self, multiplier:int) -> 'Money':
        return Franc(self._amount * multiplier)