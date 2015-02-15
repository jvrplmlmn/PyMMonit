#!/usr/bin/env python

import sys

from pymmonit import __version__, __author__
try:
    from setuptools import setup
except ImportError:
    print("PyMMonit requires setuptools in order to build. Install it using"
            " your package manager (usually python-setuptools) or via pip (pip"
            " install setuptools).")
    sys.exit(1)

setup(name='PyMMonit',
      version=__version__,
      description='MMonit API wrapper written in Python',
      author=__author__,
      author_email='javier.palomo.almena@gmail.com',
      url='https://github.com/jvrplmlmn/PyMMonit',
      license='GPLv3',
      )