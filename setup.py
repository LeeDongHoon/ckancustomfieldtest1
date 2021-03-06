from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-MYEXTENSION',
	version=version,
	description="description",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='ldhspace',
	author_email='ldhspace@yahoo.co.kr',
	url='www.naver.com',
	license='free',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.MYEXTENSION'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	usmetadata=ckanext.MYEXTENSION.plugin:USMetadataPlugin
	""",
)
