from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from os import path
from django.conf import settings
from users.models import Hackathons, ParticipatingOrganizations
import pymorphy3
from django.utils.translation import gettext as _

morph = pymorphy3.MorphAnalyzer()
# Create your views here.
def index(request):
    hackaton = Hackathons.objects.all()[0]

    start = hackaton.start_date
    start_month = _(start.strftime("%B"))
    start_parsed_month = morph.parse(start_month)[0]
    start_month_name = start_parsed_month.inflect({'gent'}).word

    end = hackaton.end_date
    end_month = _(end.strftime("%B"))
    end_parsed_month = morph.parse(end_month)[0]
    end_month_name = end_parsed_month.inflect({'gent'}).word

    return render(request, 'hackaton/index.html', {
        'hackaton': hackaton.name,
        'start': start.strftime("%d ") + start_month_name,
        'end': end.strftime("%d ") + end_month_name,
        'date': start,
    })

def partners(request):
    return render(request, 'hackaton/partners.html', {
        'orgs':ParticipatingOrganizations.objects.all(),
    })

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