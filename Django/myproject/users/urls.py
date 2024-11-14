from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
]
