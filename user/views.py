from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import LoginForm, UserForm

class UserRegister(View):

  def get(self, request):
    context = { 'form': UserForm() }
    return render(request, 'user/register.html', context)

  def post(self, request):
    form = UserForm(request.POST)

    if form.is_valid():
      user = form.save()
      user.is_active = True
      user.is_staff = True
      user.save()
      return redirect('login')
    else:
      context = { 'form': form }
      return render(request, 'user/register.html', context)

class UserLogin(View):

  def get(self, request):
    context = { 'form': LoginForm() }
    return render(request, 'user/login.html', context)

  def post(self, request):
    form = LoginForm(request.POST)

    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('/')
    else:      
      context = { 'form': form }
      return render(request, 'user/login.html', context)

class UserLogout(LoginRequiredMixin, View):

  def get(self, request):
    logout(request)
    return redirect('/')