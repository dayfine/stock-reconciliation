from random import randint, sample, choice


CASH_TRANS = ['DEPOSIT', 'FEE']
NONCASH_TRANS = ['BUY', 'SELL', 'DIVIDEND']
CASH = 'Cash'

def make_symbol():
    l = randint(1, 4)
    symbol = ''
    for _ in range(l):
        code = 96 + randint(1, 26)
        symbol += chr(code)

    return symbol.upper()


def make_symbols():
    l = randint(8, 20)
    symbols = [make_symbol() for _ in list(range(l))]
    return list(set([CASH] + symbols))


def make_pos(symbols):
    l = len(symbols)
    choices = randint(int(l * .5), int(l * .8))
    choosed = sample(symbols, choices)
    return { sym: randint(10, 500)*10 for sym in choosed }


def make_type(isCash):
    return choice(CASH_TRANS) if isCash else choice(NONCASH_TRANS)


def make_trn(symbol):
    isCash = symbol == CASH
    trans_type = make_type(isCash)
    quantity = 0
    if trans_type=='BUY' or trans_type=='SELL':
        quantity = randint(10, 1000)*10
    amount = randint(100, 5000)*10
    return [ symbol, trans_type, quantity, amount ]


def make_trns(symbols):
    l = randint(100, 1000)
    return [ make_trn(choice(symbols)) for _ in range(l) ]
