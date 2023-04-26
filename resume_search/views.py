from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage


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

def about(request):
    return HttpResponse("This is Information Page")

def services(request):
    return HttpResponse("This is Services Page")