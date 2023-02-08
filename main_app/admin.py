from django.contrib import admin
from .models import Projects, Cars, Environments, Characters

# Register your models here.
admin.site.register(Projects)
admin.site.register(Cars)
admin.site.register(Environments)
admin.site.register(Characters)