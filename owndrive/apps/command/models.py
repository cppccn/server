from django.db import models

# Create your models here.
class BaseCommand:
	def __init__(self, full_name):
		this.full_name = full_name
		this.name = getName(full_name)

	def execute(self):
		print "executing"