class Report():
    def __init__(self):
        """ Initiate a txt reader that constructs a report object """
        self.__state = None
        self.__lines = []

        self.beg_pos = {}
        self.transactions = []
        self.end_pos = {}

    def read_file(self):
        pass
        f.readline()


    def _parseStr(self):
        pass

    def _dictify(self):
        pass

    def _split(self, text):
        lines = map(str.strip, text.split('\n'))
        return [ l.split(' ') for l in lines if len(l)>0 ]
