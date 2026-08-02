from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('download-resume', views.download_resume, name = "download_resume"),
    path("contact/", views.contact, name="contact"),
]