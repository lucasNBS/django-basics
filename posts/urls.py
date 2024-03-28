from django.urls import path

from .views import PostList, PostDetailView, PostDelete, PostCreate, PostUpdate

urlpatterns = [
  path('', PostList.as_view(), name="posts"),
  path('post/<int:id>', PostDetailView.as_view(), name="post"),
  path('post/remove/<int:id>', PostDelete.as_view(), name="post-delete"),
  path('post/create/', PostCreate.as_view(), name="post-create"),
  path('post/edit/<int:id>', PostUpdate.as_view(), name="post-edit")
]
