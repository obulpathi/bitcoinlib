#!/usr/bin/env python

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README')) as f:
    README = f.read()

requires = []

setup(name='bitcoinlib',
    version='0.0.1',
    description='A Python implementation of Bitcoin library.',
    long_description=README.md,
    classifiers=[
      "Programming Language :: Python",
      ],
    url='https://github.com/obulpathi/bitcoinlib',
    author = "Obulpathi N Challa",
    author_email = "obulpathi@gmail.com",
    keywords='bitcoin',
    packages=find_packages(),
    zip_safe=False,
    install_requires=requires,
    test_suite="bitcoin.tests"
)
