from django.shortcuts import render

# Create your views here.

def wildPage(request):
    return render(request, 'index.html')

def wildPage2(request):
    return render(request, 'index2.html')