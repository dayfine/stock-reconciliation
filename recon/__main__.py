import asyncio

from .report_reader import Report
from sys import argv

script, filename = argv

#with open
txt = open(filename)

print(txt.read())
