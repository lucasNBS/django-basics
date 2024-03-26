from django.urls import path

from .views import list_posts, post, delete_post, create_post, edit_post

urlpatterns = [
  path('', list_posts, name="posts"),
  path('post/<int:id>', post, name="post"),
  path('post/remove/<int:id>', delete_post, name="post-delete"),
  path('post/create/', create_post, name="post-create"),
  path('post/edit/<int:id>', edit_post, name="post-edit")
]
