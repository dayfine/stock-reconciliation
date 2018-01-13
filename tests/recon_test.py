from recon.recon import process_trns, dict_diff, reconcile_pos
from recon.report_reader import Report

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

class TestRecon():
    def test_simple_recons(self):

        report1 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 100, 3000]],
                         end_pos={'Cash': 3000})
        result1 = {}
        assert reconcile_pos(report1) == result1

        report2 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 100, 3000]],
                         end_pos={'Cash': 2999})
        result2 = {'Cash': 1}
        assert reconcile_pos(report2) == result2

        report3 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 200, 6000]],
                         end_pos={'Cash': 6000})
        result3 = {'AAPL': -100}
        assert reconcile_pos(report3) == result3
