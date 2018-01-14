import os
import random

from recon.report_reader import Report


class TestMain():
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
        report6.read_file(TEST1)

        result6 = {'ABX': 1, 'TLT': 1, 'UA': -2, 'X': -2001, 'Cash': 6}
        # assert report6.reconcile() == result6


    def test_random(self):
        #20 random tests
        pass
