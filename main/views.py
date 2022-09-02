from django.shortcuts import render
from django.views import generic
from .service import get_all_or_filter
from .models import Sensor


class SensorListView(generic.ListView):
    """ Представление списка датчиков """
    template_name = 'main/index.html'
    context_object_name = 'sensors'

    def get_queryset(self, *, object_list=None, **kwargs):
        return get_all_or_filter(Sensor)
