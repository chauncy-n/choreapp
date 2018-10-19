from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Chore, Child, Reward
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ChildCreate(CreateView):
    model = Child
    fields = ['name','points']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.parent = self.request.user
        self.object.save()
        return HttpResponseRedirect('/user/' + str(self.object.parent))

@method_decorator(login_required, name='dispatch')
class ChildUpdate(UpdateView):
    model = Child
    fields = ['name','points','chores']

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/children/' + str(self.object.pk))

@method_decorator(login_required, name='dispatch')   
class ChildDelete(DeleteView):
    model = Child
    success_url = '/'  
@method_decorator(login_required, name='dispatch')   
class ChoreCreate(CreateView):
    model = Chore
    fields = '__all__'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/user/' + str(self.object.user))

@method_decorator(login_required, name='dispatch')
class ChoreUpdate(UpdateView):
    model = Chore
    fields = ['task', 'description', 'points']

@method_decorator(login_required, name='dispatch')
class ChoreDelete(DeleteView):
    model = Chore
    success_url = '/chores'

@method_decorator(login_required, name='dispatch')   
class RewardCreate(CreateView):
    model = Reward
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class RewardUpdate(UpdateView):
    model = Reward
    fields = ['description', 'points']

@method_decorator(login_required, name='dispatch')
class RewardDelete(DeleteView):
    model = Reward
    success_url = '/rewards'

def index(request):
    return render(request,'index.html')

@login_required(login_url='/login/')
def chores_index(request):
    chores = Chore.objects.all()
    return render(request, 'chores/index.html', {'chores': chores})

@login_required(login_url='/login/')
def chores_detail(request, chore_id):
    chore = Chore.objects.get(id=chore_id)
    return render(request, 'chores/detail.html', {'chore': chore})

@login_required(login_url='/login/')
def children_index(request):
    children = Child.objects.all()
    return render(request, 'children/index.html', {'children': children})

@login_required(login_url='/login/')
def children_detail(request, child_id):
    child = Child.objects.get(id=child_id)
    chores = child.chores.all()
    return render(request, 'children/detail.html', {'child': child, 'chores':chores})

@login_required(login_url='/login/')
def rewards_index(request):
    rewards = Reward.objects.all()
    return render(request, 'rewards/index.html', {'rewards': rewards})

@login_required(login_url='/login/')
def rewards_detail(request, reward_id):
    reward = Reward.objects.get(id=reward_id)
    return render(request, 'rewards/detail.html', {'reward': reward})

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

@login_required(login_url='/login/')
def profile(request, username):
    if username == request.user.username:
        user = User.objects.get(username=username)
        children = Child.objects.filter(parent=user)
        chores = Chore.objects.filter(user=user)
        return render(request, 'profile.html', {'username': username, 'children': children, 'chores': chores})
    else:
        return HttpResponseRedirect('/')

