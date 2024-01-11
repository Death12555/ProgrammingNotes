from django.shortcuts import render
from django.http import HttpResponse
from .models import Features


def index(request):           #To be put in views.py
    features= Features.objects.all()
    
    return render(request, 'index.html', {'features': features})