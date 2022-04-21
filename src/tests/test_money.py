from bank import Bank
from expresion.expresion import Expresion
from expresion.money import Money
from expresion.sum import Sum


def test_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.dollar(5) != OtherClass(5)
    assert Money.franc(5) != Money.dollar(5)


def test_currency():
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()


def test_simple_addition():
    five = Money.dollar(5)
    # sum = five.plus(five)
    sum = Expresion.sum(five, five)

    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reduced

def test_plus_return_sum():
    five = Money.dollar(5)
    result = Expresion.sum(five, five)

    assert type(result) is Sum and five == result.augend
    assert type(result) is Sum and five == result.addend


class OtherClass():
    def __init__(self, amount: int) -> None:
        self.__amount = amount
