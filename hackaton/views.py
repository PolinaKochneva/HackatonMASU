from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from os import path
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'hackaton/index.html')

def partners(request):
    return render(request, 'hackaton/partners.html')

def open_pdf(request):

    return render(request, 'hackaton/polozhenie.html', {
        'file':f'hackaton/{request.resolver_match.url_name}.pdf'
    })

def info(request):
    return render(request, 'hackaton/info.html')
def registration(request):
    return render(request, 'hackaton/registration.html', {
        'registration':True,
    })