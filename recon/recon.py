DEBITS = set('DEPOSIT', 'BUY')
CREDITS = set('FEE', 'SELL')

def process_trns(beg_pos, transactions):
    """ Apply each transaction to a deepcopy of the portoflio """
    end_pos = copy.deepcopy(beg_pos)

    for trans in transactions:
        symbol, trans_type, num_contracts, amount = trans.split(' ')

        # m for multiplier
        m = 1 if trans_type in DEBITS else -1 if trans in CREDITS else 0

        if symbol == 'Cash':
            end_pos['Cash'] = end_pos.get('Cash', 0) + m * amount
        else:
            end_pos[symbol] = end_pos.get(symbol, 0) + m * num_contracts
            end_pos['Cash'] = end_pos.get('Cash', 0) - m * amount

    return end_pos

def reconcile_pos(reported):
    beg_pos, end_pos = dictify(reported.beg_pos), dictify(reported.end_pos)
    calculated_end_pos = process(beg_pos, reported.transactions)

    # draw diff
    return { }
