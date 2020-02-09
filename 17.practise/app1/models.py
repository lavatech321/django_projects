

from django.db import models

class Details(models.Model):
	
	states = [
		('Maharashtra','Maharashtra'),
		('Goa','Goa'),
		('UP','Uttar Pradesh')
	]
	
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=50)
	confirm_password = models.CharField(max_length=50)
	address1 = models.CharField(max_length=200)
	address2 = models.CharField(max_length=200)
	phone_number = models.IntegerField()
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50 , 
		choices=states, default='UP')

	zip1 = models.IntegerField()
	checkbox = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)+' '+self.name

	def __iter__(self):
		for field_name in self._meta.get_fields():
			last = str(field_name).split('.')[-1]
			value = getattr(self, last, None)
			yield (field_name, value)
