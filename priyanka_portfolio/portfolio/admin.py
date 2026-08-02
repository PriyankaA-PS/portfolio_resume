from multiprocessing.reduction import register

from .models import  ContactMessage
from django.contrib import admin

admin.site.register(ContactMessage)