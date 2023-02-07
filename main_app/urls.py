from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_index, name='index'),
    path('projects/create', views.ProjectCreate.as_view(), name='funko_create'),
    path('projects/<int:projects_id>/', views.projects_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cars/', views.CarIndex.as_view(), name='car_index'),
    path('assets/', views.Index.as_view(), name='asset_index'),
    path('cars/create', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name='car_detail'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name='car_delete'),
]