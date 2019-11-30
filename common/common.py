from collections import namedtuple

Account = namedtuple("Account", "trading_type login password investor_password")
Symbol = namedtuple("Symbol", "symbol_type symbol_name")


NETTING_ACCOUNT = Account("netting", "22722541", "hz8phdia", "livjdf2b")
NETTING_SYMBOLS = Symbol("instant_ex", "EURUSD")
