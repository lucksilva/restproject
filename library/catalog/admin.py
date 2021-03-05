from django.contrib import admin

from .models import Author, Book

classe = [Author, Book]

for model in classe:
    admin.site.register(model)
