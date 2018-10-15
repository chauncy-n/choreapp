from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Chore
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class ChoreCreate(CreateView):
    model = Chore
    fields = ['task', 'description', 'points']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/chores/')

class ChoreUpdate(UpdateView):
    model = Chore
    fields = ['task', 'description', 'points']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object = self.request.user
        self.object.save()
        return HttpResponseRedirect('/chores/' + str(self.object.pk))


class ChoreDelete(DeleteView):
    model = Chore
    success_url = '/chores'

def index(request):
    return render(request,'base.html')

def chores_index(request):
    chores = Chore.objects.all()
    return render(request, 'chores/index.html', {'chores': chores})

def chores_detail(request, chore_id):
    chore = Chore.objects.get(id=chore_id)
    return render(request, 'chores/detail.html', {'chore': chore})

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def profile(request, username):
    if username == request.user.username:
        user = User.objects.get(username=username)
        chores = Chore.objects.filter(user=user)
        return render(request, 'profile.html', {'username': username, 'chores': chores})
    else:
        return HttpResponseRedirect('/')


    