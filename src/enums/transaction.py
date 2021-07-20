from enum import Enum, unique


class BaseEnum(Enum):
    def describe(self):
        return self.name, self.value

    def __str__(self):
        return "%s=%S" % (self.name,self.value)


@unique
class TransactionType(BaseEnum):
    TWONE = "21"
    TWTHREE = "23"


@unique
class TransactionMarket(BaseEnum):
    SH = "1"
    SZ = "2"
    IB = "7"
    OTC = "8"
    BC = "10"