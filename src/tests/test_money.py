from expresion.expresion import Money, Sum, Bank


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
    sum = five.plus(five)

    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reduced


def test_plus_return_sum():
    five = Money.dollar(5)
    result = five.plus(five)

    assert type(result) is Sum and five == result.augend
    assert type(result) is Sum and five == result.addend


def test_reduce_sum():
    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, "USD")
    assert Money.dollar(7) == result


def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result


def test_reduce_money_different_currency():
    bank = Bank()
    bank.addRate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")

    assert Money.dollar(1) == result


def test_identity_rate():
    bank = Bank()
    assert 1 == bank.rate("USD", "USD")


def test_mix_addition():
    fiveDollar = Money.dollar(5)
    tenFranc = Money.franc(10)

    bank = Bank()
    bank.addRate("CHF", "USD", 2)

    result = bank.reduce(fiveDollar.plus(tenFranc), "USD")

    assert Money.dollar(10) == result


def test_sum_plus_money():
    fiveBucks = Money.dollar(5)
    tenFrancs = Money.franc(10)

    bank = Bank()
    bank.addRate("CHF", "USD", 2)

    sum = Sum(fiveBucks, tenFrancs).plus(fiveBucks)
    result = bank.reduce(sum, "USD")

    assert Money.dollar(15) == result


def testSumTimes():
    fiveBucks = Money.dollar(5)
    tenFrancs = Money.franc(10)

    bank = Bank()
    bank.addRate("CHF", "USD", 2)

    sum = Sum(fiveBucks, tenFrancs).times(2)
    result = bank.reduce(sum, "USD")

    assert Money.dollar(20) == result


class OtherClass():
    def __init__(self, amount: int) -> None:
        self.__amount = amount
