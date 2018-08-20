import os
import re
import sys

from setuptools import setup, find_packages

install_requires = [
    'click',
    'requests',
    'crayons',
    'asciitree'
]

setup(
    name = 'jt',
    version = '1.0',
    url = '',
    author = '',
    author_email = '',
    packages = find_packages(),
    install_requires = install_requires,
    setup_requires = [],
    tests_require = ['pytests', 'responses'],
    zip_safe = True,
    entry_points = '''
        [console_scripts]
        jt=jt:main
    '''
)
