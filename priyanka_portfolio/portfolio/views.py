from django.conf import settings
from django.http import FileResponse
import os
from .models import  ContactMessage
from django.shortcuts import render, redirect
from analytics.models import ResumeDownloadLog

def home(request):
    return  render(request, 'portfolio/index.html')
def download_resume(request):
    file_path = os.path.join(
        'portfolio',
        'static',
        'portfolio',
        'files',
        'Priyanka_PS_FAI_Epicor.pdf'
    )
    visitor = getattr(request, "visitor", None)

    if visitor:
        ResumeDownloadLog.objects.create(
            visitor=visitor,
            ip_address=visitor.ip_address,
        )

    return FileResponse(
        open(file_path, 'rb'),
        as_attachment=True,
        filename="Priyanka_PS_FAI_Epicor.pdf"
    )

def contact(request):
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"],
        message = request.POST["message"]

        ContactMessage.objects.create(name = name, email = email, message = message )
        return redirect("home")