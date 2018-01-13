import copy


DEBITS = set(['DEPOSIT', 'BUY'])
CREDITS = set(['FEE', 'SELL', 'DIVIDEND'])
CASH = 'Cash'


def process_trns(beg_pos, transactions):
    """ Apply each transaction to a deepcopy of the portoflio """
    end_pos = copy.deepcopy(beg_pos)

    for symbol, trans_type, num_contracts, amount in transactions:
        # m for multiplier
        m = 1 if trans_type in DEBITS else -1

        if symbol != CASH:
            end_pos[symbol] = end_pos.get(symbol, 0) + m * float(num_contracts)
            m *= -1
        end_pos[CASH] = end_pos.get(CASH, 0) + m * float(amount)

    return end_pos


def dict_diff(calculated, compareTo):
    """ Modify calculated dict in place for reported valus """
    for symbol in compareTo:
        calculated[symbol] = calculated.get(symbol, 0) - compareTo[symbol]
        if calculated[symbol] == 0:
            del calculated[symbol]
    return calculated


def reconcile_pos(report):
    """ Reconcile the passed-in instance of Report object """
    calculated_end_pos = process_trns(report.beg_pos, report.transactions)

    return dict_diff(rcalculated_end_pos, eport.end_pos)
