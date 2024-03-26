from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def list_posts(request):
  posts = Post.objects.all()

  context = {
    'posts': posts
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
  return render(request, 'posts/form.html')