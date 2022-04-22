import abc


class Expresion(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def plus(self, addend: 'Expresion') -> 'Expresion':
        pass

    @abc.abstractmethod
    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        pass

    @abc.abstractmethod
    def times(self, multiplier: int) -> 'Expresion':
        pass


class Money(Expresion):
    _currency: str
    _amount: int

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, "CHF")

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> Expresion:
        return Money(self._amount * multiplier, self._currency)

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        rate = bank.rate(self._currency, to)

        return Money(int(self._amount / rate), to)

    def currency(self) -> str:
        return self._currency

    def amount(self) -> int:
        return self._amount

    def plus(self, addend: Expresion) -> Expresion:
        return Sum(self, addend)

    def __eq__(self, __o: object) -> bool:
        if type(__o) is not Money:
            return False

        return self._amount == __o._amount and self._currency == __o._currency

    def __str__(self) -> str:
        return '[amount]' + str(self._amount) + ':' + '[currency]' + self._currency


class Sum(Expresion):
    augend: Expresion
    addend: Expresion

    def __init__(self, augend: Expresion, addend: Expresion) -> None:
        self.augend = augend
        self.addend = addend

    def plus(self, addend: Expresion) -> Expresion:
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expresion:
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))

    def reduce(self, bank: 'Bank', to: str) -> Money:
        amount = self.augend.reduce(bank, to).amount() + self.addend.reduce(bank, to).amount()

        return Money(int(amount), to)


class Bank:
    __rates: dict[tuple[str, str], int]

    def __init__(self) -> None:
        self.__rates = dict()

    def reduce(self, source: Expresion, to: str) -> Money:
        return source.reduce(self, to)

    def rate(self, fromCurrency: str, toCurrency: str) -> int:
        if (fromCurrency == toCurrency):
            return 1

        return self.__rates[(fromCurrency, toCurrency)]

    def addRate(self, fromCurrency: str, toCurrency: str, rate: int) -> None:
        self.__rates[(fromCurrency, toCurrency)] = rate
