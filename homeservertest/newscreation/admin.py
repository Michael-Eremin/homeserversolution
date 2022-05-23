from django.contrib import admin

# Register your models here.
from .models import NewsLink, Category

admin.site.register(NewsLink)
admin.site.register(Category)