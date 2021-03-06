#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = [
    'Jinja2',
    'bs4',
    'python-dateutil',
    'requests'
]

test_requirements = []

setup(
    name='mka',
    version='0.8.6',
    description="Generates analysis pipelines from templates.",
    long_description=readme + '\n\n',
    author="The Parker Lab",
    author_email='parkerlab-software@umich.edu',
    url='https://github.com/ParkerLab/mka',
    packages=['mka'],
    package_data={
        'mka': ['templates/*']
    },
    scripts=[
        'scripts/fetchgeo',
        'scripts/mka',
        'scripts/mkgi',
        'scripts/screname'
    ],
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3+",
    zip_safe=False,
    keywords='mka analysis pipeline ngs atac-seq rna-seq',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
