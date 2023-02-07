from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

PURPOSE = (('3d', '3D Video Games'),
           ('2g', '2D Video Games'),
           ('V', 'Video'),
           ('N', 'NFT'),
           )

class Cars(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trim = models.CharField(max_length=100)
    date = models.DateField('Date Created') 
    file = models.FileField(upload_to='blender_files/')
    description = models.TextField(max_length=255, blank=True)
    
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.id})
    
class Buildings(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField('Date Created')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='blender_files/')
    description = models.TextField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("buildings_detail", kwargs={"pk": self.id})
    
class Environments(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField('Date Created')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='blender_files/')
    description = models.TextField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("environment_detail", kwargs={"pk": self.id})
    
class Characters(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField('Date Created')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='blender_files/')
    description = models.TextField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("character_detail", kwargs={"pk": self.id})

     
class Projects(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField('Date Created')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=2,
                               choices=PURPOSE,
                               default=PURPOSE[0][0])
    cars = models.ManyToManyField(Cars)
    buildings = models.ManyToManyField(Buildings)
    environment = models.ManyToManyField(Environments)
    character = models.ManyToManyField(Characters)
    description = models.TextField(max_length=500)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"project_id": self.id})
    
class EditCars(models.Model):
    date = models.DateField('Date Editted')
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.date}'
    
    class Meta:
        ordering = ('-date',)
        
class EditBuildings(models.Model):
    date = models.DateField('Date Editted')
    building = models.ForeignKey(Buildings, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.date}'
    
    class Meta:
        ordering = ('-date',)
        
class EditEnvironments(models.Model):
    date = models.DateField('Date Editted')
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.date}'
    
    class Meta:
        ordering = ('-date',)
        
class EditCharacters(models.Model):
    date = models.DateField('Date Editted')
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.date}'
    
    class Meta:
        ordering = ('-date',)
        
class EditProjects(models.Model):
    date = models.DateField('Date Editted')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.date}'
    
    class Meta:
        ordering = ('-date',)
    