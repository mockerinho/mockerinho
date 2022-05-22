#!/usr/bin/env python3
"""
* Install with pip (recommended):
    pip3 install .
* Install with setuptools:
    python3 setup.py install
"""
from setuptools import setup, find_packages

from mockerinho import __version__


def get_install_requires(requirements_filename: str) -> 'list[str]':
    install_requires = []
    with open(requirements_filename) as f:
        for requirement in f.readlines():
            install_requires.append(requirement)
    return install_requires


setup(
    name='mockerinho',
    description='Lightweight tool designed to simulate web API endpoints.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    version=__version__,
    url='https://github.com/mockerinho/mockerinho',
    author='Mikhail Eremeev',
    author_email='meremeev@sfedu.ru',
    license='MIT',
    platforms=('any',),
    packages=find_packages(exclude=('tests',)),
    python_requires='>=3.7,<=3.10',
    install_requires=get_install_requires('requirements.txt'),
)
