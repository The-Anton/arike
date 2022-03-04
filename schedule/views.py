from django.shortcuts import render

from django.views.generic.list import ListView

from schedule.models import Visit

class GenericScheduleListView(ListView):
    model = Visit
    context_object_name = 'visits'
    qureyset = Visit.objects.all()
    template_name = 'schedule/schedule_list.html' 
