from expresion.expresion import Expresion
from expresion.money import Money


class Sum(Expresion):
    augend: Money
    addend: Money

    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend = augend
        self.addend = addend
