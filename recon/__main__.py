"""
Main Program to be run in CLI via
`python3  -m recon yourfile.txt`

"""

from .report_reader import Report
from sys import argv

script, filename = argv

#with open
txt = open(filename)

print(txt.read())
