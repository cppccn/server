from django.test import TestCase
import logging
from django.test import Client
from django.contrib.auth.models import User
from cappuccino import local_settings
from cappuccino.apps.command.commands import CommandParams
import os
import json
import shutil

class CommandTestCase(TestCase):
	def setUp(self):
		self.TEST_DIRNAME = '_command-test-directory'
		self.SYSTEM_PATH_TEST_DIR = local_settings.SHARED_PATH + self.TEST_DIRNAME

		# Creating test dir
		if not os.path.exists(self.SYSTEM_PATH_TEST_DIR):
		    os.makedirs(self.SYSTEM_PATH_TEST_DIR)

	# Retrieves the Response object to the CommandRequest
	def sendCommandRequest(self, params):
		# Making ls request and checking response code
		c = Client()
		response = c.get('/command/', params)
		return response

	def tearDown(self):
		if not os.path.exists(self.SYSTEM_PATH_TEST_DIR):
			shutil.rmtree(self.SYSTEM_PATH_TEST_DIR)


class LsCommandTestCase(CommandTestCase):
	def setUp(self):
		super(LsCommandTestCase, self).setUp()
		# setUp -> test_ls_no_args
		for i in range(0,5): # Creating 5 files in SHARED_PATH named PREFIX1.txt to PREFIX5.txt
			open(local_settings.SHARED_PATH + '/' + self.TEST_DIRNAME + str(i) + '.txt', 'w')

		# setUp -> test_ls_path
		for i in range(0,5): # Creating 5 files in SHARED_PATH named PREFIX1.txt to PREFIX5.txt
			open(local_settings.SHARED_PATH + '/' + self.TEST_DIRNAME + '/' + str(i) + '.txt', 'w')

	def test_ls_no_args(self):
		# Making ls request and checking response code
		params = CommandParams('ls', '/').toDict()
		response = super(LsCommandTestCase, self).sendCommandRequest(params)
		self.assertTrue(response.status_code, 200)
		
		# Test all created files are there
		files_json = response.json()['data']
		filenames = [f['name'] for f in files_json]
		self.assertTrue(self.TEST_DIRNAME in filenames, True)

		for i in range(0, 5):
			filename = self.TEST_DIRNAME + str(i) + '.txt'
			self.assertTrue(True if filename in filenames else False, True)

	def test_ls_parent_dir(self):
		# Making ls request and checking response code
		params = CommandParams('ls', '/').toDict()
		response = super(LsCommandTestCase, self).sendCommandRequest(params)
		self.assertTrue(response.status_code, 200)

		print(response)
		# Executing 'ls' from the root, or an 'ls ..' from one level subdir, should give the same response
		params = CommandParams('ls ..', self.SYSTEM_PATH_TEST_DIR).toDict()
		response_back = super(LsCommandTestCase, self).sendCommandRequest(params)
		self.assertTrue(response_back.status_code, 200)
		print(response_back)

		self.assertTrue(response, response_back)

	def test_ls_path(self):
		# Making ls request and checking response code
		params = CommandParams('ls', '/' + self.TEST_DIRNAME).toDict()
		response = super(LsCommandTestCase, self).sendCommandRequest(params)
		self.assertTrue(response.status_code, 200)

		# Test all created files are there
		files_json = response.json()['data']
		filenames = [f['name'] for f in files_json]

		for i in range(0, 5):
			filename = str(i) + '.txt'
			self.assertTrue(True if filename in filenames else False, True)

	def test_ls_current_path(self):
		# Making ls request and checking response code
		params = CommandParams('ls', '/').toDict()
		response = super(LsCommandTestCase, self).sendCommandRequest(params)
		self.assertTrue(response.status_code, 200)

		# Executing 'ls' from the root, or an 'ls ..' from one level subdir, should give the same response
		params = CommandParams('ls .', '/').toDict()
		response_back = super(LsCommandTestCase, self).sendCommandRequest(params)
		self.assertTrue(response_back.status_code, 200)

		self.assertTrue(response, response_back)

	def tearDown(self):
		super(LsCommandTestCase, self).tearDown()

		# tearDown -> test_ls_no_args
		for i in range(0, 5):
			os.remove(local_settings.SHARED_PATH + '/' + self.TEST_DIRNAME + str(i) + '.txt')

		# tearDown -> test_ls_path
		for i in range(0, 5):
			os.remove(local_settings.SHARED_PATH + '/' + self.TEST_DIRNAME + '/' + str(i) + '.txt')