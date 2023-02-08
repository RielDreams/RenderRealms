from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_index, name='index'),
    path('projects/create', views.ProjectCreate.as_view(), name='funko_create'),
    path('projects/<int:projects_id>/', views.projects_detail, name='detail'),
    path('projects/<int:projects_id>/add_editting/', views.add_editting, name='add_editting'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cars/', views.CarIndex.as_view(), name='car_index'),
    path('cars/create', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name='car_detail'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name='car_delete'),
    path('environments/', views.EnvironmentIndex.as_view(), name='environment_index'),
    path('environments/create', views.EnvironmentCreate.as_view(), name='environment_create'),
    path('environments/<int:pk>/', views.EnvironmentDetail.as_view(), name='environment_detail'),
    path('environments/<int:pk>/update', views.EnvironmentUpdate.as_view(), name='environment_update'),
    path('environments/<int:pk>/delete', views.EnvironmentDelete.as_view(), name='environment_delete'),
]