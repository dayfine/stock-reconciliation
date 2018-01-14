"""
Main Program to be run in CLI via
`python3  -m recon yourfile.txt`
"""

from os.path import join, dirname
from pathlib import Path

from sys import argv
from .report_reader import Report

script, filename = argv


# Check if it's absolute path
# If not, points to this module's root directory
if not Path(filename).exists:
    filename = join(dirname(dirname(__file__)), filename)
report = Report()
report.read_file(filename)


print('Reading and reconciling {}'.format(filename))
print('===================')

differences = report.reconcile()
output_text = []
print('Please review the reconciled differences:')
print('-------------------')

for k, v in differences.items():
    line = '{} {}'.format(k, v)
    print(line)
    output_text.append(line)

print('-------------------')


name, extension = filename.split('.')
output = ''.join([name, '_output.', extension])

with open(output, 'w') as f:
    f.write('\n'.join(output_text))

