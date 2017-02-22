# coding=utf-8

"""
A setuptools based setup module.

See:
    https://packaging.python.org/en/latest/distributing.html
    https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path
import nfox


READ_ME = 'README.md'
PATH = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(PATH, READ_ME), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='NFox',

    # Versions MUST comply with PEP440.
    #   https://www.python.org/dev/peps/pep-0440/
    #
    # Versions MUST also follow the Semantic Versioning Specification
    #   http://semver.org/
    #
    # For a discussion on single-sourcing the version across setup.py
    # and the project code, see:
    #   https://packaging.python.org/en/latest/single_source_version.html
    version=nfox.__version__,

    description='A media information utility.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/pynfox/nfox',

    # Author details
    author='Labrys',
    author_email='Labrys.git@gmail.com',

    # Choose the project license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who this project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Video',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Indicate the supported operating systems
        'Operating System :: OS Independent',

        # Pick a license as for the project (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions supported here.
        # Indicate whether Python 2, Python 3 or both are supported.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # What does this project relate to?
    keywords='metadata movie multimedia nfo series tv video',

    # Specify the packages manually here if this project is simple
    # or use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List run-time dependencies here.  These will be installed by pip when
    # this project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    tests_require=[
        'flake8_docstrings',
        'flake8-import-order',
        'pep8-naming',
        'pycodestyle',
        'pydocstyle',
        'pytest',
        'pytest-cov',
        'pytest-flake8',
        'tox',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). They can be installed using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': [],
    },
)
