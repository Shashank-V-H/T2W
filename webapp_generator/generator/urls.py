from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for the index page
    path('generate/', views.generate_webpage, name='generate_webpage'),
    path('download_zip/', views.download_zip, name='download_zip'),  # Route for ZIP download
    path('about_us/',views.about_us, name='about_us')
]
