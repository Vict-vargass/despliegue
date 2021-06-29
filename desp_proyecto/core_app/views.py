from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core_app/index.html')

def inicio_real(request):
    return render(request, 'core_app/home.html')