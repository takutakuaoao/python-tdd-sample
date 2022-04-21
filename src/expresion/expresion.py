import abc

from expresion.money import Money
from expresion.sum import Sum


class Expresion(metaclass=abc.ABCMeta):
    @staticmethod
    def sum(augend: Money, addend: Money) -> 'Expresion':
        return Sum(augend, addend)
