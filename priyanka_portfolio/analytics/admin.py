from django.contrib import admin
from .models import Visitor, ResumeDownloadLog

admin.site.register(Visitor)
admin.site.register(ResumeDownloadLog)