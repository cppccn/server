from django.test import TestCase
import logging
from django.test import Client
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
	def test_login(self):
		"""
		Tests that the user can correctly log in
		"""
		user = User.objects.create_superuser(username='testuser', password='12345', email="test-email@gmail.com")
		user.save()

		c = Client()
		response = c.post('/login/', {'username': 'testuser', 'password': '12345'})
		self.assertTrue(response.status_code, 200)