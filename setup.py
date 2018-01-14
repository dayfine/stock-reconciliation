
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))


# class PyTest(TestCommand):


packages = []

requires = []

test_requirements = ['pytest>=2.8.0']

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)


setup(
    name='Stock Reconciliaton',
    description=about['__description__'],
    long_description=long_description,
    author=about['__author__'],
    url=about['__url__'],
    packages=packages,
    install_requires=requires,
    include_package_data=True,
    cmdclass={
        'test': PyTest,
    },
    tests_require=test_requirements,
)
