


from expresion.expresion import Expresion
from expresion.money import Money


class Bank:
    def reduce(self, source: Expresion, to: str) -> Money:
        return Money.dollar(10)