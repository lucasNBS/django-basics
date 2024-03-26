from django.urls import path

from .views import list_posts, post, delete_post, create_post, edit_post

urlpatterns = [
  path('', list_posts, name="posts"),
  path('<int:id>', post, name="post"),
  path('remove/<int:id>', delete_post, name="post-delete"),
  path('create/', create_post, name="post-create"),
  path('edit/<int:id>', edit_post, name="post-edit")
]
