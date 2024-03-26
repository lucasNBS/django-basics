from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def list_posts(request):
  posts = Post.objects.all()

  paginator = Paginator(posts, 2)

  page = request.GET.get('page')

  if page == 0 or page is None:
    page = 1

  page_obj = paginator.get_page(page)

  context = {
    'page_obj': page_obj
  }

  return render(request, 'posts/index.html', context)

def post(request, id):
  post = Post.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'posts/post.html', context)

def delete_post(request, id):
  post = get_object_or_404(Post, id=id)
  post.delete()
  return redirect('posts')

def create_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      form = PostForm()
      return redirect('posts')
  else:
    form = PostForm()

  context = {
    'form': form
  }

  return render(request, 'posts/form.html', context)

def edit_post(request, id):
  post = get_object_or_404(Post, id=id)

  if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      form = PostForm(instance=post)
      return redirect('posts')
  else:
    form = PostForm(instance=post)

  context = {
    "form": form
  }

  return render(request, 'posts/form.html', context)