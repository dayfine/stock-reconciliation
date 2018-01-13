class Report():
    def __init__(self, beg_pos={}, transactions=[], end_pos={}):
        """ Initiate a txt reader that constructs a report object """
        self._state = None
        self._lines = []

        self.beg_pos = beg_pos
        self.transactions = transactions
        self.end_pos = end_pos

    def read_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self._lines.append(line.strip().split())

    def _parseStr(self):
        pass

    def _dictify(self):
        pass

    def _split(self, lines):
        return [ l.strip().split(' ') for l in lines if len(l)>0 ]
