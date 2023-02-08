from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Projects, Cars, Environments, Characters

# from .forms import 
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'assetmodels'

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

def projects_index(request):
    projects = Projects.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def projects_detail(request, projects_id):
    project = Projects.objects.get(id=projects_id)
    return render(request, 'projects/detail.html', {'project': project})
    
    
class ProjectCreate(CreateView):
    model = Projects
    fields = ['name', 'date', 'purpose']
    success_url = '/projects/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProjectUpdate(UpdateView):
    model = Projects
    fields = '__all__'
    
class ProjectDelete(DeleteView):
     model = Projects
     success_url = '/projects/'
     


class CarIndex(LoginRequiredMixin, ListView):
    model = Cars


class CarCreate(LoginRequiredMixin, CreateView):
    model = Cars
    fields = ['file', 'name', 'brand', 'trim', 'date', 'description']
    
    
    def form_valid(self, form):
        
        form.instance.user = self.request.user
        blender_file = self.request.FILES.get('blender-file', None)
        if blender_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + blender_file.name[blender_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(blender_file, BUCKET, key)
                url = f"{S3_BASE_URL}{BUCKET}/{key}"
                form.instance.url = url
            except:
                print('An error occurred uploading file to S3')
        return super().form_valid(form)
    
    

class CarDetail(LoginRequiredMixin, DetailView):
    model = Cars
    sucessful_url = '/cars/'


class CarDelete(LoginRequiredMixin, DeleteView):
    model = Cars
    success_url = '/cars/'


class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Cars
    fields = '__all__'
    
    
class EnvironmentIndex(LoginRequiredMixin, ListView):
    model = Environments


class EnvironmentCreate(LoginRequiredMixin, CreateView):
    model = Environments
    fields = ['file', 'name', 'date', 'description']
    
    
    def form_valid(self, form):
        
        form.instance.user = self.request.user
        blender_file = self.request.FILES.get('blender-file', None)
        if blender_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + blender_file.name[blender_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(blender_file, BUCKET, key)
                url = f"{S3_BASE_URL}{BUCKET}/{key}"
                form.instance.url = url
            except:
                print('An error occurred uploading file to S3')
        return super().form_valid(form)
    
    

class EnvironmentDetail(LoginRequiredMixin, DetailView):
    model = Environments
    sucessful_url = '/Environments/'


class EnvironmentDelete(LoginRequiredMixin, DeleteView):
    model = Environments
    success_url = '/Environments/'


class EnvironmentUpdate(LoginRequiredMixin, UpdateView):
    model = Environments
    fields = '__all__'   



def add_editting(request, project_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.project_id = project_id
        new_cleaning.save()
    return redirect('detail', project_id=project_id)
    
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