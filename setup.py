# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ard/__init__.py
from ard import __version__ as version

setup(
	name='ard',
	version=version,
	description='ARD Settings ',
	author='ARD',
	author_email='Hadeel.milad@ard.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
