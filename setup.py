
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    pass

test_requirements = ['pytest>=2.8.0']

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='Stock Reconciliaton',
    description='Reconcile stock transactions',
    long_description=long_description,
    author='Di Fan',
    url='https://github.com/dayfine/stock-reconciliation',
    packages=[],
    install_requires=[],
    include_package_data=True,
    # cmdclass={
    #     'test': PyTest,
    # },
    tests_require=test_requirements,
)
