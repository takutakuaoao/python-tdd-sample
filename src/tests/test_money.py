from money import Dollar, Franc, Money


def test_multiplication():
    five = Money.dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)


def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    assert Dollar(5) != OtherClass(5)

    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    assert Franc(5) != OtherClass(5)

    assert Franc(5) != Dollar(5)

def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)

class OtherClass():
    def __init__(self, amount:int) -> None:
        self.__amount = amount