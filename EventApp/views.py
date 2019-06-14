from django.shortcuts import render
from django.http import HttpResponse
from .models import EventApp

# Create your views here.
def index(request):

    events = EventApp.objects.all()
    context = {
        'events': events
    }
    return render(request, 'EventApp/index.html', context)

def details(request, id):
    event = EventApp.objects.get(id=id)
    context = {
        'event': event
    }
    return render(request, 'EventApp/details.html', context)
