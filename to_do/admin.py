from atexit import register
from django.contrib import admin
from .models import ToDo

admin.site.register(ToDo)