from django.test import TestCase
import logging
from django.test import Client
from django.contrib.auth.models import User
from cappuccino import local_settings
import os
import json

class LsCommandTestCase(TestCase):
	def setUp(self):
		self.TEST_DIR = local_settings.SHARED_PATH + '/lscommand-test-dir'
		self.FILE_PREFIX = 'lscommand-test-'

		# Creating test dir
		if not os.path.exists(self.TEST_DIR):
		    os.makedirs(self.TEST_DIR)

		# Creating 5 files inside named 1.txt to 5.txt
		for i in range(0,5):
			open(local_settings.SHARED_PATH + '/' + self.FILE_PREFIX + str(i) + '.txt', 'w')

	def test_ls_no_args(self):
		# Making ls request and checking response code
		c = Client()
		response = c.get('/command/', {'command': 'ls', 'currentDir': '/'})
		self.assertTrue(response.status_code, 200)
		
		# Test all created files are there
		files_json = response.json()['data']
		print("File Json: ")
		print(files_json)

		#files_dict = json.loads(files_json)
		filenames = [f['name'] for f in files_json]
		print(filenames)

		# Check setUp files info retrieved
		dirname = self.FILE_PREFIX +'dir'
		self.assertTrue(dirname in filenames, True)


		for i in range(0, 5):
			filename = self.FILE_PREFIX + str(i) + '.txt'
			self.assertTrue(True if filename in filenames else False, True)

	def tearDown(self):
		print("TearDown method called")
		dirname = self.FILE_PREFIX +'dir'

		# Clean up
		for i in range(0, 5):
			os.remove(local_settings.SHARED_PATH + '/' + self.FILE_PREFIX + str(i) + '.txt')
		os.rmdir(local_settings.SHARED_PATH + '/' + dirname)