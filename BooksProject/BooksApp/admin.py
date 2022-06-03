from django.contrib import admin
from django.contrib import admin
from setuptools import Command
from .models import Books, Comments

admin.site.register(Books)
admin.site.register(Comments)

