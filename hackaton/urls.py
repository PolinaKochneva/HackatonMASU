from django.urls import path
from . import views

app_name = 'hackaton'

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("partners/", views.partners, name="partners"),
    path("info/", views.info, name="info"),
]