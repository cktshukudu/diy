from cgitb import html
from django.shortcuts import render
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from .models import webSite

# Create your views here.

# Create your views here.
#@descript login/landing page
#@ GET /
def landing(request):
    print(request)
    return render(request,'diy/tourism/home.html')

def create(request):
 if request.method == 'POST':
    
    heading=request.POST.get('heading')
    url=request.POST.get('url')
    subHead=request.POST.get('subHead')
    content1=request.POST.get('content1')
    content2=request.POST.get('content2') 
    content3=request.POST.get('content3')
    content4=request.POST.get('content4')
    aboutUs=request.POST.get('aboutUs')
    adrs1=request.POST.get('adrs1')
    adrs2=request.POST.get('adrs2')
    adrs3=request.POST.get('adrs3')
    celNo=request.POST.get('celNo')
    email=request.POST.get('email')

    content={'heading':heading,
    'url':url,
    'subHead':subHead,
    'content1':content1,
    'content2':content2,
    'content3':content3,
    'content4':content4,
    'aboutUs':aboutUs,
    'adrs1':adrs1,
    'adrs2':adrs2,
    'adrs3':adrs3,
    'celNo':celNo,
    'email':email}
    
    companyName=request.POST.get('companyName')

    html_content=render_to_string("medic/medic.html",{'content':content}) 


    user=webSite.objects.create(
        htmlString=html_content,
        companyName=companyName
    )
    return render(request,'medic/view.html',{'body':html_content})
    
def createWebString(request):
      if request.method == 'POST':
         heading=request.POST.get('heading')
         image1=request.POST.get('image1')
         image2=request.POST.get('image2')
         image3=request.POST.get('image3')
         image4=request.POST.get('image4')
         price1=request.POST.get('price1')
         price2=request.POST.get('price2')
         price3=request.POST.get('price3')
         price4=request.POST.get('price4')
         product1=request.POST.get('product1')
         product2=request.POST.get('product2')
         product3=request.POST.get('product3')
         product4=request.POST.get('product4')
         subHead=request.POST.get('subHead')
         content1=request.POST.get('content1')
         content2=request.POST.get('content2') 
         content3=request.POST.get('content3')
         header1=request.POST.get('header1')
         header2=request.POST.get('header2') 
         header3=request.POST.get('header3')
         aboutUs=request.POST.get('aboutUs')
         adrs1=request.POST.get('adrs1')
         adrs2=request.POST.get('adrs2')
         adrs3=request.POST.get('adrs3')
         celNo=request.POST.get('celNo')
         email=request.POST.get('email')

         content={'heading':heading,
          'image1':image1,
          'image2':image2,
          'image3':image3,
          'image4':image4,
          'price1':price1,
          'price2':price2,
          'price3':price3,
          'price4':price4,
          'product1':product1,
          'product2':product2,
          'product3':product3,
          'product4':product4,
          'subHead':subHead,
          'content1':content1,
          'content2':content2,
          'content3':content3,
          'header1':header1,
          'header2':header2,
          'header3':header3,
          'aboutUs':aboutUs,
          'adrs1':adrs1,
         'adrs2':adrs2,
         'adrs3':adrs3,
         'celNo':celNo,
         'email':email}
         companyName=request.POST.get('companyName') 
         html_content=render_to_string("diy/tourism/tourism.html",{'content':content}) 
         user=webSite.objects.create(
         htmlString=html_content,
         companyName=companyName
         )

         return render(request,'diy/completed.html',{'body':html_content,'companyName':companyName})
      return render(request,'diy/tourism/create.html')

def webSites(request,cName):
    html_content=webSite.objects.get(companyName=cName).htmlString
    #print(html_content)
    return render(request,'diy/medic/view.html',{'container':html_content,'companyName':cName})