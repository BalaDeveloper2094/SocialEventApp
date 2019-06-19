from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.db.models import Count
from .models import EventApp, EventAppPolling
from .forms import DateForm

# Create your views here.
def index(request):

    events = EventApp.objects.all()
    context = {
        'events': events
    }
    return render(request, 'EventApp/index.html', context)

def details(request, id):
    event = EventApp.objects.get(id=id)
    requestedEventName = EventApp.objects.values_list('title', flat=True).get(id=id)
    topDates = EventAppPolling.objects.values('datePicker', 'eventName').filter(eventName=requestedEventName).annotate(c=Count('datePicker')).order_by('-c')[:4]
    dates = DateForm()
    context = {
        'event': event,
        'dates': dates,
        'topDates' : topDates
    }
    return render(request, 'EventApp/details.html', context)

def AddEventPolling(request, id): 
    if request.method == 'POST':
        inputname = request.POST['inputname']
        datePicker = request.POST['datePicker']
        if EventAppPolling.objects.filter(inputname=request.POST['inputname']).exists():
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            eventName = EventApp.objects.values_list('title', flat=True).get(id=id)
            addEventPollingDate = EventAppPolling(inputname=inputname, datePicker=datePicker, eventName=eventName)
            addEventPollingDate.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
