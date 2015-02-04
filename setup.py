#!/usr/bin/env python
"""
Flask-GeoIP
-------------

Simple Flask extension for pygeoip.
"""
from __future__ import print_function
import codecs
import os
from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages


appname = 'Flask-GeoIP'
pkgname = appname.lower().replace('-', '_')
metadata_relpath = '{}/metadata.py'.format(pkgname)

# Get package metadata. We use exec here instead of importing the
# package directly, so we can avoid any potential import errors.
with open(metadata_relpath) as fh:
    metadata = {}
    exec(fh.read(), globals(), metadata)


def read(fn):
    with codecs.open(fn, 'r', 'utf-8') as fh:
        contents = fh.read()
    return contents


setup(
    name=appname,
    version=metadata['__version__'],
    description=__doc__,
    long_description=read(os.path.join(os.path.dirname(__file__),
                                       'README.md')),
    packages=find_packages(),
    install_requires = [str(ir.req) for ir
                                    in parse_requirements('requirements.txt', session=PipSession())],
    entry_points={
        'console_scripts': {
            # Add console scripts here. E.g:
            # 'cleanup = mypkg.bin.cleanup:main',
        },
    },
    author='Jacob Magnusson',
    author_email='m@jacobian.se',
    url='https://github.com/jmagnusson/Flask-GeoIP',
    license='BSD',
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
