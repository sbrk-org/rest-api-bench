OB#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import imp
from pip.req import parse_requirements
from setuptools import setup, find_packages


sys.path.append(os.path.abspath(os.path.dirname(__file__)))


MODULE_NAME = 'pathwar_api'
MODULE = imp.load_module(MODULE_NAME, *imp.find_module(MODULE_NAME))


DEPENDENCIES = [
    'flask >=0.10.1',
    'flask-classy >= 0.6',
    'fluent-logger >=0.3.3, ==github',
    'voluptuous >=0.8.1',
    'Flask-SQLAlchemy >=1.0',
    'Flask-AlchemyView >=0.1.4'
]


setup(
    name=MODULE_NAME,
    version=MODULE.__version__,
    description='Pathwar API server',
    author='Pathwar',
    author_email='contact@pathwar.net',
    url='http://pathwar.net/',
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    tests_require=DEPENDENCIES + ['nose', 'coverage', 'mock'],
    dependency_links=[],
    test_suite=MODULE_NAME + '.tests',
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: System :: Distributed Computing',
    ],
    license='Proprietary',
    entry_points={
        'console_scripts': [
            'pathwar-api = pathwar_api.bin.wsgi:main',
        ],
    },
)
