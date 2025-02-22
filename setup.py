#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='uncurl',
    version='0.0.11',
    description='A library to convert curl requests to python-requests.',
    author='Steve Pulec',
    author_email='spulec@gmail.com',
    url='https://github.com/XMYSTERlOUSX/uncurl',
    entry_points={
        'console_scripts': [
            'uncurl = uncurl.bin:main',
        ],
    },
    install_requires=['pyperclip', 'six'],
    packages=find_packages(exclude=("tests", "tests.*")),
)
