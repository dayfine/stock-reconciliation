import os
import asyncio

from recon.recon import _process_trns, _dict_diff


class TestRecon():
    def test_transaction_processing(self):
        #Simple test
        beg_pos = {
            'foo': 100,
            'bar': 100,
            'baz': 100,
            'moo': 100,
            'Cash': 600
        }
        trans = [
            ['foo' , 'BUY', 75, 500],
            ['foo' , 'SELL', 125, 600],
            ['Cash' , 'FEE', 0, 100],
            ['bar' , 'SELL', 100, 700],
            ['moo' , 'BUY', 75, 100],
            ['baz' , 'SELL', 125, 400],
            ['qux' , 'SELL', 100, 300],
            ['ham' , 'BUY', 100, 500],
            ['ham' , 'SELL', 75, 500],
        ]
        end_pos = _process_trns(beg_pos, trans)

        assert end_pos['foo'] == 50
        assert end_pos['bar'] == 0
        assert end_pos['baz'] == -25
        assert end_pos['moo'] == 175
        assert end_pos['qux'] == -100
        assert end_pos['ham'] == 25
        assert end_pos['Cash'] == 1900

    def test_dictionary_differentiation(self):
        #Simple test 1
        dict_1a = {'foo': 100, 'bar': 100}
        dict_1b = {'foo': 200, 'baz': 100}

        result1 = {'foo': 100, 'bar': -100, 'baz': 100}
        assert _dict_diff(dict_1a, dict_1b) == result1

        #Simple test 2
        dict_1a = {'foo': 100, 'bar': 100, 'baz': 100}
        dict_1b = {'foo': 100, 'bar': 100}

        result1 = {'baz': -100}
        assert _dict_diff(dict_1a, dict_1b) == result1

        #Simple test 3
        dict_1a = {'foo': 100, 'bar': 100}
        dict_1b = {'foo': 100, 'bar': 100, 'baz': 100}

        result1 = {'baz': 100}
        assert _dict_diff(dict_1a, dict_1b) == result1
