import os
import logging
from random import randint, sample, choice
from copy import deepcopy

from recon.report_reader import Report
from tests.utils import make_symbols, make_pos, make_trns


class TestReportReader():
    def test_simpler(self):
        #Simpler test 1
        report1 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 100, 300]],
                         end_pos={'Cash': 300})
        result1 = {}
        assert report1.reconcile() == result1

        #Simpler test 2
        report2 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 100, 300]],
                         end_pos={'Cash': 299})
        result2 = {'Cash': -1}
        assert report2.reconcile() == result2

        #Simpler test 3
        report3 = Report(beg_pos={'AAPL': 100},
                         transactions=[['AAPL', 'SELL', 200, 600]],
                         end_pos={'Cash': 600})
        result3 = {'AAPL': 100}
        assert report3.reconcile() == result3

        #Simpler test 4
        report4 = Report(beg_pos={'AAPL': 100},
                         transactions=[['GOOG', 'SELL', 200, 600]],
                         end_pos={'AAPL': 100, 'Cash': 600})
        result4 = {'GOOG': 200}
        assert report4.reconcile() == result4


    def test_simple(self):
        #Simple test 1 using text file input
        TEST1 = os.path.join(os.path.dirname(__file__), 'test1.txt')
        report5 = Report()
        report5.read_file(TEST1)

        result5 = {'Cash': 8000, 'GOOG': 10, 'TD': -100, 'MSFT': 10}
        assert report5.reconcile() == result5

        #Simple test 2 using text file input
        TEST2 = os.path.join(os.path.dirname(__file__), 'test2.txt')
        report6 = Report()
        report6.read_file(TEST2)

        result6 = {'ABX': 1, 'TLT': 1, 'UA': -2, 'X': -2001, 'Cash': -994}
        assert report6.reconcile() == result6


    def test_random(self):
        CASH = 'Cash'

        # 20 random tests
        for i in range(20):

            symbols = make_symbols()
            beg_pos, trns = make_pos(symbols), make_trns(symbols)
            end_pos = deepcopy(beg_pos)

            if CASH not in end_pos:
                end_pos[CASH] = 0

            # explictly process each transaction
            for sym, typ, quat, amt in trns:
                if typ == 'BUY':
                    end_pos[sym] = end_pos.get(sym, 0) + quat
                    end_pos[CASH] -= amt

                elif typ == 'SELL':
                    end_pos[sym] = end_pos.get(sym, 0) - quat
                    end_pos[CASH] += amt

                elif typ == 'DIVIDEND':
                    end_pos[CASH] += amt

                elif typ == 'DEPOSIT':
                    end_pos[CASH] += amt

                elif typ == 'FEE':
                    end_pos[CASH] -= amt

            for sym in list(end_pos):
                if end_pos[sym] == 0:
                    del end_pos[sym]

            report = Report(beg_pos = beg_pos,
                            transactions = trns,
                            end_pos = end_pos)
            result = {}

            assert report.reconcile() == result
