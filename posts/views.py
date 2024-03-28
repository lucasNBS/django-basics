from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostList(ListView):
  model = Post
  template_name = 'posts/index.html'
  paginate_by = 2

  def get_queryset(self):
    query_set = super().get_queryset()

    search_author = self.request.GET.get('search-author')
    search_title = self.request.GET.get('search-title')

    if search_author is not None and search_author is not '':
      query_set = query_set.filter(user__username=search_author)
    if search_title is not None and search_title is not '':
      query_set = query_set.filter(title__icontains=search_title)

    return query_set

  def get_context_data(self, **kwargs):
    context = super(ListView, self).get_context_data(**kwargs)

    users = []

    for post in self.model.objects.all():
      if post.user not in users:
        users.append(post.user)

    context['users'] = users

    search_author = self.request.GET.get('search-author')
    search_title = self.request.GET.get('search-title')

    if search_author is None:
      search_author = ""
    if search_title is None:
      search_title = ""

    context['search_author'] = search_author
    context['search_title'] = search_title

    return context

class PostDetailView(DetailView):
  model = Post
  pk_url_kwarg = 'id'
  template_name = 'posts/post.html'

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('posts')
  login_url = '/login'
  template_name = 'posts/confirm_delete.html'

  def get(self, request, *args, **kwargs):
    post = self.get_object()

    if request.user == post.__getattribute__('user'):
      return super().get(request, *args, **kwargs)
    
    return redirect('posts')

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  login_url = '/login'
  template_name = 'posts/form.html'
  form_class = PostForm
  success_url = reverse_lazy('posts')

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  login_url = '/login'
  pk_url_kwarg = 'id'
  template_name = 'posts/form.html'
  form_class = PostForm
  success_url = reverse_lazy('posts')

  def get(self, request, *args, **kwargs):
    post = self.get_object()

    if request.user == post.__getattribute__('user'):
      return super().get(request, *args, **kwargs)
    
    return redirect('posts')