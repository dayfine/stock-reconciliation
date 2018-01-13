from helpers import dictify
from recon import process_trns, reconcile_pos
from sys import argv
script, filename = argv

#with open
txt = open(filename)

print(txt.read())
