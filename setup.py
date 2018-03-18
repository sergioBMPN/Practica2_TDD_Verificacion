# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Practica 2 TDD',
    long_description=readme,
    author='Miguel Muniz',
    author_email='miguel.muniz@u-tad.live.com',
    packages=find_packages(exclude=('tests', 'docs'))
)