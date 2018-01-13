from recon.recon import process_trns, dict_diff, reconcile_pos

BEG_POS = {
    'AAPL': 15,
    'GOOG': 25,
    'SPY': 170,
    'Cash': 3500
}

END_POS = {
    'AAPL': 190,
    'GOOG': 134,
    'SPY': 170,
    'Cash': 3500,
    'TD': 99
}

T1 = [
    ['AAPL', 'SELL', 100, 30000],
    ['GOOG', 'BUY', 10, 10000],
    ['Cash', 'DEPOSIT', 0, 1000],
    ['Cash', 'FEE', 0, 50],
    ['GOOG', 'DIVIDEND', 0, 50],
    ['TD', 'BUY', 100, 10000],
]

# class TestRecon():
    # def test_recon(self):
    #     report1 = {}
    #     result1 = {}
    #     assert reconcile_pos(report1) == result1
