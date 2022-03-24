from django.shortcuts import render
from .forms import ContactForm
import mimetypes
from django.http.response import HttpResponse
import os

# Create your views here.


def index(request):
    return render(request, "diy/base.html", {})

def home(request):
    return render(request, "diy/home.html", {})

def education(request):
    return render(request, "diy/education.html", {})

def log(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'logistics.zip'
    filepath = BASE_DIR + '/diy/file/' + filename
    path = open(filepath, errors="ignore")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def medical(request):
    return render(request, "diy/medical.html", {})

def cleaning(request):
    return render(request, "diy/cleaning.html", {})

def med(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'medic.zip'
    filepath = BASE_DIR + '/diy/file/' + filename
    path = open(filepath, errors="ignore")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def tourism(request):
    return render(request, "diy/tourism.html", {})

def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'diy/contact.html', context)

def edu(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'diy_websites.zip'
    filepath = BASE_DIR + '/diy/file/' + filename
    path = open(filepath, errors="ignore")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def clean(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'diy_websites.zip'
    filepath = BASE_DIR + '/diy/file/' + filename
    path = open(filepath, errors="ignore")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
