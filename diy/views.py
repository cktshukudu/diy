from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "diy/base.html", {})

def home(request):
    return render(request, "diy/home.html", {})

def education(request):
    return render(request, "diy/education.html", {})

def beauty(request):
    return render(request, "diy/beauty.html", {})

def medical(request):
    return render(request, "diy/medical.html", {})

def cleaning(request):
    return render(request, "diy/cleaning.html", {})

def ngo(request):
    return render(request, "diy/ngo.html", {})

def tourism(request):
    return render(request, "diy/tourism.html", {})
