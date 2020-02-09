

from django.db import models

class Details(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	active = models.BooleanField() # required=False makes the field optional
	created_on = models.DateTimeField()
	last_logged_in = models.DateTimeField()

	def __str__(self):
		return str(self.id)+' '+self.name