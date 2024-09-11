from django.contrib import admin
from main.models import *
# Register your models here.

model_list = [Author, News, Category]
admin.site.register(model_list)