from stock_reconciliation.recon import process_trns, reconcile_pos

BEG_POS
END_POS

T1
T2
T3


example1 = {
    'beg_pos': {
        'AAPL': 15,
        'GOOG': 25,
        'SPY': 170,
        'Cash': 3500
    },
    'transactions': [
        ['AAPL', 'SELL', 100, 30000],
        ['GOOG', 'BUY', 10, 10000],
        ['Cash', 'DEPOSIT', 0, 1000],
        ['Cash', 'FEE', 0, 50],
        ['GOOG', 'DIVIDEND', 0, 50],
        ['TD', 'BUY', 100, 10000],
    ],
    'end_pos': {
        'AAPL': 190,
        'GOOG': 134,
        'SPY': 170,
        'Cash': 3500,
        'TD': 99
    }
}


print(reconcile_pos(example_reports))
