from django.urls import path
from . import views

app_name = 'hackaton'

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("partners/", views.partners, name="partners"),
    path("info/", views.info, name="info"),
    path("polozhenie_nordhack/", views.open_pdf, name="polozhenie_nordhack"),
    path("day1/", views.open_pdf, name="day1"),
    path("day2/", views.open_pdf, name="day2"),
    path("day3/", views.open_pdf, name="day3"),
]