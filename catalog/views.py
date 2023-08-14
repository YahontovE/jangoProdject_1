from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contact_info(request):
    return render(request,'catalog/contact_info.html')
