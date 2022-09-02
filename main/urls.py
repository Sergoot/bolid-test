from django.urls import path
from .views import SensorListView

urlpatterns = [
    path('', SensorListView.as_view(), name='sensors_list')
]
