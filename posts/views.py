from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def list_posts(request):
  posts = Post.objects.all()

  users = []

  for post in posts:
    if post.user not in users:
      users.append(post.user)

  search_title = request.GET.get("search-title")
  search_author = request.GET.get("search-author")

  if search_title is not None:
    posts = posts.filter(title__icontains=search_title)
  if not search_author == "" and not search_author is None:
    posts = posts.filter(user__username=search_author)

  paginator = Paginator(posts, 2)

  page = request.GET.get('page')

  if page == 0 or page is None:
    page = 1

  if search_title is None:
    search_title = ""
  if search_author is None:
    search_author = ""

  page_obj = paginator.get_page(page)

  context = {
    'page_obj': page_obj,
    'search_title': search_title,
    'users': users,
    'search_author': search_author,
  }

  return render(request, 'posts/index.html', context)

def post(request, id):
  post = Post.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'posts/post.html', context)

@login_required(login_url='/login')
def delete_post(request, id):
  post = get_object_or_404(Post, id=id)

  if post.user != request.user:
      return redirect('posts')

  post.delete()
  return redirect('posts')

@login_required(login_url='/login')
def create_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.instance.user = request.user
      form.save()
      form = PostForm()
      return redirect('posts')
  else:
    form = PostForm()

  context = {
    'form': form
  }

  return render(request, 'posts/form.html', context)

@login_required(login_url='/login')
def edit_post(request, id):
  post = get_object_or_404(Post, id=id)

  if post.user != request.user:
    return redirect('posts')

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