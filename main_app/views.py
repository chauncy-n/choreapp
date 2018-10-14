from django.shortcuts import render
from django.http import HttpResponse
from .models import Chore

# Create your views here.

def index(request):
    return render(request,'base.html')

def chores_index(request):
    chores = Chore.objects.all()
    return render(request, 'chores/index.html', {'chores': chores})

class ChoreCreate(CreatView):
    model = Chore
    fields = [task, description, points]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object = self.request.user
        self.object.save()
        return HttpResponseRedirect('/chores/')