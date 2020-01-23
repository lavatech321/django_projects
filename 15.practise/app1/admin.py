
from django.contrib import admin
from .models import Event
from .models import Person
from .models import Identity

admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Identity)

# Register your models here.
