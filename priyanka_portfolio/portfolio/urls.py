from django.urls import path
# from . import views
from  .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('download-resume', download_resume, name = "download_resume"),
    path("contact/", contact, name="contact"),
]