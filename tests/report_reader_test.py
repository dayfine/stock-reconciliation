from recon.report_reader import Report
transactions = """
    NVDA SELL 212 3412
    VRX BUY 10 4323
    Cash DEPOSIT 0 1000.45
    Cash FEE 0 502
    GOOG DIVIDEND 0 50
    ABX BUY 100 1430
    CHK BUY 1023 3194
    UA SELL 24 140
"""

class TestReportReader():

    def test_split_long_string_into_lines_of_tokens(self):
        report = Report()
        splitted = report._split(transactions)

        assert len(splitted) == 8
        assert all([len(x)==4 for x in splitted]) == True