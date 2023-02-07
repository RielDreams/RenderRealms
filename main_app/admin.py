from django.contrib import admin
from .models import Projects, Cars, Buildings, Environments, Characters

# Register your models here.
admin.site.register(Projects)
admin.site.register(Cars)
admin.site.register(Buildings)
admin.site.register(Environments)
admin.site.register(Characters)