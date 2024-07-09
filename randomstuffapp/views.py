from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

# Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@ensure_csrf_cookie
def get_csrf_token(request):
  return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})

def home(request):
  return render(request, "home.html")

def todos(request):
  items = TodoItem.objects.all()
  return render(request, "todos.html", {"todos": items})

def register(request): 
  form = CreateUserForm()
  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('my-login')

  context = {'registerform': form}

  return render(request, 'randomstuffapp/register.html', context=context)

def my_login(request):
  form = LoginForm()
  if request.method == "POST":
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        auth.login(request, user)
        return redirect("dashboard")
  
  context = {'loginform': form}

  return render(request, 'randomstuffapp/my-login.html', context=context)

def user_logout(request):
  auth.logout(request)
  return redirect("home")

@login_required(login_url="my-login")
def dashboard(request):
  return render(request, 'randomstuffapp/dashboard.html')