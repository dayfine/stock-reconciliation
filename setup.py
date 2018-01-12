
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from io import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

NAME = 'Stock Reconciliaton'

here = os.path.abspath(os.path.dirname(__file__))


# class PyTest(TestCommand):


packages = []

requires = []

test_requirements = ['pytest>=2.8.0']

with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)


setup(
    name=NAME,
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    install_requires=requires,
    include_package_data=True,
    license=about['__license__'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'test': PyTest,
    },
    tests_require=test_requirements,
)
