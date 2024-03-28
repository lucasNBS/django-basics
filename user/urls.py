from django.urls import path

from .views import UserRegister, UserLogin, UserLogout

urlpatterns = [
  path('login/', UserLogin.as_view(), name="login"),
  path('register/', UserRegister.as_view(), name="register"),
  path('logout/', UserLogout.as_view(), name="logout"),
]
