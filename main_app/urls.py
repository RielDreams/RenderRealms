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
    path('cars/create', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/', views.CarDetail.as_view(), name='car_detail'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name='car_delete'),
    path('characters/', views.CharacterIndex.as_view(), name='character_index'),
    path('characters/create', views.CharacterCreate.as_view(), name='character_create'),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name='character_detail'),
    path('characters/<int:pk>/update', views.CharacterUpdate.as_view(), name='character_update'),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(), name='character_delete'),
    path('Buildings/', views.BuildingIndex.as_view(), name='Building_index'),
    path('Buildings/create', views.BuildingCreate.as_view(), name='Building_create'),
    path('Buildings/<int:pk>/', views.BuildingDetail.as_view(), name='Building_detail'),
    path('Buildings/<int:pk>/update', views.BuildingUpdate.as_view(), name='Building_update'),
    path('Buildings/<int:pk>/delete', views.BuildingDelete.as_view(), name='Building_delete'),
        path('envorinments/', views.EnvorinmentIndex.as_view(), name='envorinment_index'),
    path('envorinments/create', views.EnvorinmentCreate.as_view(), name='envorinment_create'),
    path('envorinments/<int:pk>/', views.EnvorinmentDetail.as_view(), name='envorinment_detail'),
    path('envorinments/<int:pk>/update', views.EnvorinmentUpdate.as_view(), name='envorinment_update'),
    path('envorinments/<int:pk>/delete', views.EnvorinmentDelete.as_view(), name='envorinment_delete'),
]