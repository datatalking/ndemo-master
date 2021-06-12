from setuptools import setup

setup(
	name='ndemo-master',
	version='ndemo2.0',
	packages=['app', 'app.migrations', 'ndemo', 'ndemo.settings', 'zinnia', 'zinnia.urls', 'zinnia.admin',
	          'zinnia.tests', 'zinnia.tests.implementations', 'zinnia.tests.implementations.urls', 'zinnia.views',
	          'zinnia.views.mixins', 'zinnia.models', 'zinnia.xmlrpc', 'zinnia.management',
	          'zinnia.management.commands', 'zinnia.migrations', 'zinnia.models_bases', 'zinnia.spam_checker',
	          'zinnia.spam_checker.backends', 'zinnia.templatetags', 'zinnia.url_shortener',
	          'zinnia.url_shortener.backends'],
	url='',
	license='',
	author='wadewilson',
	author_email='AndrewSchell3@gmail.com',
	description='personal webpage'
)
