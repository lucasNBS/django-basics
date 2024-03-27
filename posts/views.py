from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def list_posts(request):
  posts = Post.objects.all()

  search_title = request.GET.get("search-title")

  if search_title is not None:
    posts = posts.filter(title__icontains=search_title)

  paginator = Paginator(posts, 2)

  page = request.GET.get('page')

  if page == 0 or page is None:
    page = 1

  if search_title is None:
    search_title = ""

  page_obj = paginator.get_page(page)

  context = {
    'page_obj': page_obj,
    'search_title': search_title,
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
    form = PostForm(request.POST, request.FILES)
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
    form = PostForm(request.POST, request.FILES, instance=post)
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