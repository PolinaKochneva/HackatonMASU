from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", views.profile, name='profile'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("addCommand", views.add_command, name='add_command'),
    path("delCommand", views.del_command, name='del_command'),
    path("addMember", views.add_member, name='add_member'),
    path("delMember", views.del_member, name='del_member'),
    path("register", views.register, name='registration'),
    path("update_user_info", views.update_user_info, name='update_user_info'),
    path("deleteUser", views.delete_user, name='delete_user'),
    path("command", views.command, name='command'),
    path("schedule", views.schedule, name='schedule'),
    path("task", views.task, name='task'),
    path("newTask", views.new_task, name='new_task'),
    path("changeTask", views.change_task, name='change_task'),
    path("newHackathon", views.new_hackathon, name='new_hackathon'),
    path("updateDateHackathon", views.update_date_hackathon, name='update_date_hackathon'),
    path("add_representative", views.add_representative, name='add_representative'),
    path("add_org", views.add_org, name='add_org'),
    path("add_task", views.add_task, name='add_task'),
]