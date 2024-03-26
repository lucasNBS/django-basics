from django.contrib import admin
from django.urls import path

from .views import list_posts, post, delete_post

urlpatterns = [
  path('', list_posts, name="posts"),
  path('<int:id>', post, name="post"),
  path('remove/<int:id>', delete_post, name="post-delete")
]
