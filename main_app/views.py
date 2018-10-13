from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'base.html')

class Chore:
    def __init__(self, task, description):
        self.task = task
        self.description = description

chores = [
    Chore('clean room', 'put everything away'),
    Chore('brush teeth', 'brush all your teeth not just two'),
]


def chores_index(request):
    return render(request, 'chores/index.html', {'chores': chores})