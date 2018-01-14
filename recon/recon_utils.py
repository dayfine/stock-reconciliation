import copy


DEBITS = set(['DEPOSIT', 'BUY'])
CREDITS = set(['FEE', 'SELL', 'DIVIDEND'])
CASH = 'Cash'


def reconcile_pos(report):
    """ Reconcile the passed-in instance of Report object """
    calculated_end_pos = _process_trns(report.beg_pos, report.transactions)

    return _dict_diff(calculated_end_pos, report.end_pos)


def _process_trns(beg_pos, transactions):
    """ Apply each transaction to a deepcopy of the portoflio """
    end_pos = copy.deepcopy(beg_pos)

    for symbol, trans_type, num_contracts, amount in transactions:
        # m for multiplier
        m = 1 if trans_type in DEBITS else -1

        if symbol != CASH:
            end_pos[symbol] = end_pos.get(symbol, 0) + m * num_contracts
            m *= -1
        end_pos[CASH] = end_pos.get(CASH, 0) + m * amount

    return end_pos


def _dict_diff(dict1, dict2):
    """ Modify dict1 in place for reported values in dict2 """
    fullList = set(list(dict1)+list(dict2))

    for symbol in fullList:
        dict1[symbol] = dict2.get(symbol, 0) - dict1.get(symbol, 0)

    for symbol in fullList:
        if dict1[symbol] == 0:
            del dict1[symbol]

    return dict1



