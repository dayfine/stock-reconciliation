ST_POS0 = 'D0-POS'
ST_TRNS = 'D1-TRN'
ST_POS1 = 'D1-POS'


class Report():
    def __init__(self, beg_pos={}, transactions=[], end_pos={}):
        """ Initiate a txt reader that constructs a report object """
        self._state = None

        self.beg_pos = beg_pos
        self.transactions = transactions
        self.end_pos = end_pos

    def read_file(self, filename):
        """ Reading text file line by line """
        with open(filename, 'r') as file:
            for line in file:
                l = line.strip()

                if line == ST_POS0:
                    self._state = ST_POS0
                elif line == ST_TRNS:
                    self._state = ST_TRNS
                elif line == ST_POS0:
                    self._state = ST_POS0
                else:
                    self._parse_line(line)

    def _parse_line(self, line):
        if not line:
            return

        if self._state == ST_POS0:
            key, val = line.split()
            self.beg_pos[key] = float(val)

        elif self._state == ST_TRNS:
            sym, typ, num, amount = line.split()
            self.transactions.append([sym, typ, float(num), float(amount)])

        elif self._state == ST_POS1:
            key, val = line.split()
            self.end_pos[key] = float(val)

    def read_text(self, text):
        """ Reading single long string line by line """
        if isinstance(text, (str, unicode)):
            lines = text.split('\n')
        else:
            lines = text

        for line in lines:
                l = line.strip()

                if line == ST_POS0:
                    self._state = ST_POS0
                elif line == ST_TRNS:
                    self._state = ST_TRNS
                elif line == ST_POS0:
                    self._state = ST_POS0
                else:
                    self._parse_line(line)
