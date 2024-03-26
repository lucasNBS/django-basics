from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, UserForm

def user_register(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      user.is_active = True
      user.is_staff = True
      user.save()

      return redirect('login')
  
  else:
    form = UserForm()

  context = {
    'form': form,
  }

  return render(request, 'user/register.html', context)

def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('/')
  
  else:
    form = LoginForm()

  context = {
    'form': form,
  }

  return render(request, 'user/login.html', context)

def user_logout(request):
  logout(request)
  return redirect('/')