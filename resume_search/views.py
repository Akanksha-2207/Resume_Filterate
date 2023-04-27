from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from resume_parser import resumeparse
from pyresparser import ResumeParser
from django.conf import settings
from django.contrib import messages
import os
from django.db import IntegrityError
from .models import Resume

# Create your views here.
def index(request):
    context={}
    if request.method == 'POST':
        uploaded_file=request.FILES['resumes']
        fs=FileSystemStorage()
        fs.save(name=uploaded_file.name,content=uploaded_file)
    return render(request,'index.html')

def upload_cv(request):
    return render(request, "Choose_File.html")

