from django.db import models
from datetime import datetime
# Create your models here.

class EventApp(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    location = models.TextField(default='')
    Date = models.DateTimeField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Event App"


class EventAppPolling(models.Model):
    inputname = models.TextField(default='')
    datePicker = models.DateField(default=datetime.now, blank=True)
    eventName = models.CharField(default='', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Event App Polling"


