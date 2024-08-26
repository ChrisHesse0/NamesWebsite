from django.urls import path

from . import views

app_name = "names"

urlpatterns = [
    path("", views.index, name="index"),
    path('get_names/', views.get_names, name='get_names'),
    path('search/', views.search_name, name='search_name'),
    path('search_results/', views.search_results, name='search_results'),
]