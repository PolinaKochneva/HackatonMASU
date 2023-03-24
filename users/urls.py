from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("addCommand", views.add_command, name='add_command'),
    path("register", views.register, name='registration'),
    path("deleteUser", views.delete_user, name='delete_user'),
    path("command", views.command, name='command'),
]