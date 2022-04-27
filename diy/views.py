from django.shortcuts import render,redirect
import mimetypes
from django.http.response import HttpResponse
import os
from cgitb import html
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from .models import webSite
# from .models import cleanSite
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from .forms import webForm
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):
    return render(request, "diy/base.html", {})

def home(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
        ['devtespace@gmail.com'], # To Email
            )

        return render(request, 'diy/home.html', {'message_name': message_name})

    else:
        return render(request, "diy/home.html", {})


def tourism(request):
    return render(request, "diy/tourism.html", {})

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

def med(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'medic.zip'
    filepath = BASE_DIR + '/diy/file/' + filename
    path = open(filepath, errors="ignore")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def education(request):
    return render(request, "diy/education.html", {})

def edu(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'edu.zip'
    filepath = BASE_DIR + '/diy/file/' + filename
    path = open(filepath, errors="ignore")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def cleaning(request):
    return render(request, "diy/cleaning.html", {})

def clean(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'cl.zip'
    filepath = BASE_DIR + '/diy/file/' + filename
    path = open(filepath, errors="ignore")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def create(request):
    if request.method == 'POST' and request.FILES['upload']:
              about=request.POST.get('about')
              upload=request.FILES.get('upload')
              activities=request.POST.get('activities')
              explore=request.POST.get('explore')
              image=request.POST.get('image')
              ply=request.POST.get('ply')
              imags=request.POST.get('imags')
              health=request.POST.get('health')
              himages=request.POST.get('himages')
              adrs1=request.POST.get('adrs1')
              adrs2=request.POST.get('adrs2')
              adrs3=request.POST.get('adrs3')
              cellno=request.POST.get('cellno')
              companyName=request.POST.get('companyName')
              fss = FileSystemStorage()
              file = fss.save(upload.name, upload)
              file_url = fss.url(file)
          
              content={'about':about,'upload':upload,'activities':activities,'explore':explore,'image':image,'ply':ply,'imags':imags,'health':health,'himages':himages,'adrs1':adrs1,'adrs2':adrs2,'adrs2':adrs1,'adrs3':adrs1,'cellno':cellno,'companyName':companyName}
              companyName = request.POST.get("companyName")
         
              html_content=render_to_string("diy/ed.html",{'content':content,'file_url':file_url }) 
              user=webSite.objects.create(htmlString=html_content,companyName=companyName)        
    return render(request,'diy/view.html',{'body':html_content})

def createWebString(request):
   return render(request,'diy/create.html')

def webSites(request,cName):
    html_content=webSite.objects.get(companyName=cName).htmlString
    # print(html_content)
    return render(request,'diy/view.html',{'container':html_content,'companyName':cName})

