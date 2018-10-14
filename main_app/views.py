from django.shortcuts import render
from django.http import HttpResponse
from .models import Chore

# Create your views here.

def index(request):
    return render(request,'base.html')

def chores_index(request):
    chores = Chore.objects.all()
    return render(request, 'chores/index.html', {'chores': chores})