from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
]
