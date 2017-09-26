# -*- coding: utf-8 -*-

import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
        
with open('README.rst') as readme_file:
    readme = readme_file.read()

#test_requirements = ['pytest', 'tox']
requirements = ['requests']
        
setup(
    name='esm_o365_cfg',
    version='0.0.1',
    description="Configures Office 365 Activity API subscriptions.",
    author="Andy Walden",
    author_email='aw@krakencodes.com',
    url='https://github.com/andywalden/esm_o365_cfg',
    packages=['esm_o365_cfg'],
    package_dir={'esm_o365_cfg': 'esm_o365_cfg'},
    entry_points = {'console_scripts': ['esm_o365_cfg=esm_o365_cfg.esm_o365_cfg:main']},
    include_package_data=True,
    install_requires=requirements,
    license="ISC",
    keywords='esm_o365_cfg',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only'],
    #test_suite='tests',
    #tests_require=test_requirements,
    python_requires='>=3')
