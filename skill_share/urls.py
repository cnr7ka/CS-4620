from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('', views.login, name="login"),
    path('create_profile/', views.create_profile, name="create_profile"),
    path('create_profile/create_skill/', views.create_skill, name="create_skill"),
]
