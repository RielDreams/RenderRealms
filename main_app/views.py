from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CarForm, EnvironmentForm, CharacterForm
import uuid
import boto3
from .models import Projects, Cars, Environments, Characters
from .forms import EditProjectsForm

# from .forms import 
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'assetmodels'

# Create your views here.
def home(request):
    cars = Cars.objects.all()
    environments = Environments.objects.all()
    character = Characters.objects.all()
    return render(request, "home.html", {'cars': cars,
                                         'environments': environments,
                                         'character': character,})

def about(request):
    return render(request, 'about.html')

def projects_index(request):
    projects = Projects.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def projects_detail(request, projects_id):
    project = Projects.objects.get(id=projects_id)
    editting_form = EditProjectsForm()
    cars_not_assign = Cars.objects.exclude(id__in = project.cars.all().values_list('id'))
    environments_not_assign = Environments.objects.exclude(id__in = project.cars.all().values_list('id'))
    return render(request, 'projects/detail.html', {'project': project,
                                                    "editting_form": editting_form,
                                                    "cars": cars_not_assign,
                                                    'environments': environments_not_assign,})

@login_required
def assoc_car(request, projects_id, car_id):
    Projects.objects.get(id=projects_id).cars.add(car_id)
    return redirect('detail', projects_id=projects_id)

@login_required
def disassoc_car(request, projects_id, car_id):
    Projects.objects.get(id=projects_id).cars.remove(car_id)
    return redirect('detail', projects_id=projects_id)
    
@login_required
def assoc_environment(request, projects_id, environment_id):
    Projects.objects.get(id=projects_id).environments.add(environment_id)
    return redirect('detail', projects_id=projects_id)

@login_required
def disassoc_environment(request, projects_id, environment_id):
    Projects.objects.get(id=projects_id).environments.remove(environment_id)
    return redirect('detail', projects_id=projects_id)

@login_required
def assoc_character(request, projects_id, character_id):
    Projects.objects.get(id=projects_id).characters.add(character_id)
    return redirect('detail', projects_id=projects_id)

@login_required
def disassoc_character(request, projects_id, character_id):
    Projects.objects.get(id=projects_id).characters.remove(character_id)
    return redirect('detail', projects_id=projects_id)


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Projects
    fields = ['name', 'date', 'purpose']
    success_url = '/projects/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Projects
    fields = '__all__'
    
class ProjectDelete(LoginRequiredMixin, DeleteView):
     model = Projects
     success_url = '/projects/'


class CarIndex(LoginRequiredMixin, ListView):
    model = Cars

class CarCreate(LoginRequiredMixin, CreateView):
    model = Cars
    form_class = CarForm
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        photo_file = self.request.FILES.get('photo', None)
        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(photo_file, BUCKET, key)
                url = f"{S3_BASE_URL}{BUCKET}/{key}"
                form.instance.photo_url = url
            except Exception as error:
                print('An error occurred uploading photo file to S3')
                print(error)
        return super().form_valid(form)

class CarDetail(LoginRequiredMixin, DetailView):
    model = Cars
    sucessful_url = '/cars/'
    
class CarDelete(LoginRequiredMixin, DeleteView):
    model = Cars
    success_url = '/cars/'

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Cars
    fields = ['name', 'brand', 'trim', 'description']


class EnvironmentIndex(LoginRequiredMixin, ListView):
    model = Environments

class EnvironmentCreate(LoginRequiredMixin, CreateView):
    model = Environments
    form_class = EnvironmentForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        photo_file = self.request.FILES.get('photo', None)
        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(photo_file, BUCKET, key)
                url = f"{S3_BASE_URL}{BUCKET}/{key}"
                form.instance.photo_url = url
            except Exception as error:
                print('An error occurred uploading photo file to S3')
                print(error)
        return super().form_valid(form)

class EnvironmentDetail(LoginRequiredMixin, DetailView):
    model = Environments
    sucessful_url = '/Environments/'

class EnvironmentDelete(LoginRequiredMixin, DeleteView):
    model = Environments
    success_url = '/environments/'

class EnvironmentUpdate(LoginRequiredMixin, UpdateView):
    model = Environments
    fields = ["name", "description"]   


class CharacterIndex(LoginRequiredMixin, ListView):
    model = Characters

class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Characters
    form_class = CharacterForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        photo_file = self.request.FILES.get('photo', None)
        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(photo_file, BUCKET, key)
                url = f"{S3_BASE_URL}{BUCKET}/{key}"
                form.instance.photo_url = url
            except Exception as error:
                print('An error occurred uploading photo file to S3')
                print(error)
        return super().form_valid(form)

class CharacterDetail(LoginRequiredMixin, DetailView):
    model = Characters
    sucessful_url = '/characters/'

class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Characters
    success_url = '/characters/'

class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Characters
    fields = ["name", "description"]   


def add_editting(request, projects_id):
    form = EditProjectsForm(request.POST)
    if form.is_valid():
        new_edits = form.save(commit=False)
        new_edits.project_id = projects_id
        new_edits.save()
    return redirect('detail', projects_id=projects_id)
    
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)