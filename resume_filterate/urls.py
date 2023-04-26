"""resume_filterate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from resume_search import views

# Manually added (Username:Admin Password:Admin)  Admin page Login Details 
admin.site.site_header = "CV Search Engine Admin"
admin.site.site_title = "CV Search Engine Admin Portal"
admin.site.index_title = "Welcome to CV Search Engine"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('resume_search.urls')),
    path('upload_cv',views.upload_cv,name='upload_cv')
]
