

from django.db import models

class Event(models.Model):
  name = models.CharField('Event Name', max_length=120)
  event_date = models.DateTimeField('Event Date')
  venue = models.CharField(max_length=120)
  manager = models.CharField(max_length = 60)
  description = models.TextField(blank=True)

  def __str__(self):
    return self.name

  def __iter__(self):
    for field_name in self._meta.get_fields():
    	last = str(field_name).split('.')[-1]
    	value = getattr(self, last, None)
    	yield (field_name, value)
 

#####  Start of OneToOne Example ##########

class Person(models.Model):
  name = models.CharField('Name',max_length=120)
  address = models.TextField(blank=True)  

  def __str__(self):
    return "ID:{}".format(self.pk)

  def __iter__(self):
    for no,field_name in enumerate(self._meta.get_fields()):
      if int(no) == 0:
        last = str(field_name).split('.')[-1][:-1]
      else:
        last = str(field_name).split('.')[-1]
      value = getattr(self, last, None)
      yield (field_name, value)


class Identity(models.Model):
  p_id = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
  adhar_card = models.CharField(max_length=32)
  pan_card = models.CharField(max_length=32)

  def __str__(self):
    return "p_id => {}, adhar_card => {}, pan_Card => {}".format(self.p_id,self.adhar_card,self.pan_card)

  def __iter__(self):
    for field_name in self._meta.get_fields():
      last = str(field_name).split('.')[-1]
      value = getattr(self, last, None)
      yield (field_name, value)
 
 #####  End of OneToOne Example ##########



#####  Start of OneToMany Example ##########

class Customer(models.Model):
  name = models.CharField('Name',max_length=120)
  phno = models.CharField(max_length=120)  

  def __str__(self):
    return "ID:{}".format(self.pk)

  def __iter__(self):
    for no,field_name in enumerate(self._meta.get_fields()):
      if int(no) == 0:
        last = str(field_name).split('.')[-1][:-1]
      else:
        last = str(field_name).split('.')[-1]
      value = getattr(self, last, None)
      yield (field_name, value)


class Order(models.Model):
  c_id = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )
  order_date = models.DateField()
  order_amount = models.CharField(max_length=32)

  def __str__(self):
    return "id => {} , c_id => {}, order_date => {}, order_amount => {}".format(self.id,self.c_id,self.order_date,self.order_amount)

  def __iter__(self):
    for field_name in self._meta.get_fields():
      last = str(field_name).split('.')[-1]
      value = getattr(self, last, None)
      yield (field_name, value)
 
 #####  End of OneToMany Example ##########

#####  Start of ManyToMany Example ##########

class Student(models.Model):
  name = models.CharField('Name',max_length=120)
  phno = models.CharField(max_length=120)  

  def __str__(self):
    return "ID:{}".format(self.pk)

  def __iter__(self):
    for no,field_name in enumerate(self._meta.get_fields()):
      if int(no) == 0:
        last = str(field_name).split('.')[-1][:-1]
      else:
        last = str(field_name).split('.')[-1]
      value = getattr(self, last, None)
      yield (field_name, value)


class Tution(models.Model):
  students = models.ManyToManyField(Student)
  subject = models.CharField(max_length=50)
  teacher = models.CharField(max_length=32)
  fees = models.CharField(max_length=32)

  def __str__(self):
    return "id => {} , subject => {}, teacher => {}, fees => {}".format(self.id,self.subject,self.teacher,self.fees)

  def __iter__(self):
    for field_name in self._meta.get_fields():
      last = str(field_name).split('.')[-1]
      value = getattr(self, last, None)
      yield (field_name, value)
 
 #####  End of ManyToMany Example ##########






