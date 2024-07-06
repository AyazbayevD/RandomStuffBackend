from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("todos/", views.todos, name="Todos"),
  path("register", views.register, name="register"),
  path("my-login", views.my_login, name="my-login"),
  path("dashboard", views.dashboard, name="dashboard"),
  path('user-logout', views.user_logout, name="user-logout"),
  path('csrf-token/', views.get_csrf_token, name='csrf-token')
]