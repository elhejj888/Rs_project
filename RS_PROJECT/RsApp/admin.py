from django.contrib import admin
from .models import Student
from .models import Professeur
from .models import Groupe

# Register your models here.
admin.site.register(Student)
admin.site.register(Professeur)
admin.site.register(Groupe)