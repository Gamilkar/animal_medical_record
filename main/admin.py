from django.contrib import admin
from main import models

admin.site.register(models.Animal)
admin.site.register(models.Treatment)
admin.site.register(models.Vaccination)
