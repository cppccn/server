from django.test import TestCase
import logging
from django.test import Client
from django.contrib.auth.models import User

class ClientTestCase(TestCase):
	def test_client_correctly_served(self):
		"""
		Tests that after the login the page which displays the list of files is correctly sent.
		"""
		# Creates a user and logs in
		user = User.objects.create_superuser(username='testuser', password='12345', email="sconqua@gmail.com")
		user.save()

		c = Client()
		response = c.post('/login/', {'username': 'testuser', 'password': '12345'})
		self.assertTrue(response.status_code, 200)

		# Checks that we have access to the main page of our web client
		response = c.get('/')
		self.assertTrue(b'<html ng-app="cappuccinoWebClient">' in response._container[0])
