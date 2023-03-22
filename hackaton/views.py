from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hackaton/index.html')

def registration(request):
    return render(request, 'hackaton/registration.html', {
        'registration':True,
    })