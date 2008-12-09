#!/usr/bin/env python

import os

from setuptools import setup, find_packages

version = '1.0.0b1'

def read_file(name):
        return open(os.path.join(os.path.dirname(__file__), name)).read()

readme = read_file('README')
install = read_file('INSTALL')
tags = read_file('TAGS')
changes = read_file('CHANGES')

setup(name='easy-yuidoc',
        version=version,
        description="yuidoc is a set of tools to generate the API documentation"
                    "for the JavaScript in the YUI library",
        long_description='\n\n'.join([readme, install, tags, changes]),
        classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Console',
                'License :: OSI Approved :: BSD License',
                'Operating System :: MacOS :: MacOS X',
                'Operating System :: Microsoft :: Windows',
                'Operating System :: POSIX',
                'Programming Language :: JavaScript',
                'Programming Language :: Python :: 2.4',
                'Programming Language :: Python :: 2.5',
                'Topic :: Software Development :: Documentation'
                ],
        package_dir={'': 'src'},
        packages=find_packages('src'),
        include_package_data = True,
        author='Damien Lebrun', # author of the setup fork only
        author_email='dinoboff@hotmail.com',
        url='http://github.com/dinoboff/yuidoc/tree/master',
        license='BSD',
        zip_safe=False,
        install_requires=['pygments','Cheetah','simplejson'],
        entry_points={
                'console_scripts': [
                        'yuidoc = yui.doc:main',
                        ],
                },
)
