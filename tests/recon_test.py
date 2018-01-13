import os

from recon.recon import process_trns, dict_diff, reconcile_pos
from recon.report_reader import Report


class TestRecon():
    def test_simplest_recons(self):
        report1 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 100, 300]],
                         end_pos={'Cash': 300})
        result1 = {}
        assert reconcile_pos(report1) == result1

        report2 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 100, 300]],
                         end_pos={'Cash': 299})
        result2 = {'Cash': -1}
        assert reconcile_pos(report2) == result2

        report3 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 200, 600]],
                         end_pos={'Cash': 600})
        result3 = {'AAPL': 100}
        assert reconcile_pos(report3) == result3

        report4 = Report(beg_pos={'AAPL': 100},
                         transactions=[['GOOG', 'SELL', 200, 600]],
                         end_pos={'AAPL': 100, 'Cash': 600})
        result4 = {'GOOG': 200}
        assert reconcile_pos(report4) == result4


    def test_simpler_recons(self):
        report = Report()
        print()
        report.read_file('test1')
        print(reconcile_pos(report))


    def test_simple_recons(self):
        pass
