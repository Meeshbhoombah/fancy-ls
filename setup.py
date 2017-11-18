# -*- encoding: utf-8 -*-
"""

"""

from setuptools import setup

setup(
    name='fancyls',
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fancyls = hello:cli
    '''
)

