from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def list_posts(request):
  posts = Post.objects.all()

  context = {
    "posts": posts
  }

  return render(request, "posts/index.html", context)

def post(request, id):
  post = Post.objects.get(id=id)

  context = {
    "post": post
  }

  return render(request, "posts/post.html", context)

def delete_post(request, id):
  post = get_object_or_404(Post, id=id)
  post.delete()
  return redirect('posts')