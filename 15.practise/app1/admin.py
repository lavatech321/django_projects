
from django.contrib import admin
from .models import Event
from .models import Person
from .models import Identity
from .models import Student
from .models import Tution
from .models import Test
from .models import Test2

admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Identity)
admin.site.register(Student)
admin.site.register(Tution)
admin.site.register(Test)
admin.site.register(Test2)

# Register your models here.
