from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for the index page
    path('generate/', views.generate_webpage,name='generate_webpage'),
]
