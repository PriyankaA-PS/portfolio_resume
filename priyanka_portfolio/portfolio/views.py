from django.conf import settings
from django.http import FileResponse
import os

from django.shortcuts import render


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

    return FileResponse(
        open(file_path, 'rb'),
        as_attachment=True,
        filename="Priyanka_PS_FAI_Epicor.pdf"
    )