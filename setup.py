#!/usr/bin/env python

from setuptools import setup, find_packages
from fdra import __version__


setup(
    name='fdra',
    version=__version__,
    description='FDR-based p-value adjuster',
    packages=find_packages(),
    author='Daichi Narushima',
    author_email='dnarsil+github@gmail.com',
    url='https://github.com/dceoy/fdra',
    include_package_data=True,
    install_requires=['pandas'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    long_description="""\
fdra
-----

FDR-based p-value adjuster
"""
)
