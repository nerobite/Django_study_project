from .views import SensorListCreateView
from django.urls import path
from .views import SensorUpdateView, MeasurementCreateView, SensorRetrieveView, SensorCreateView, SensorListView

urlpatterns = [
    path('home/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('sensors/create/', SensorCreateView.as_view(), name='sensor-create'),
    path('sensors/<int:pk>/', SensorUpdateView.as_view(), name='sensor-update'),
    path('sensors/<int:pk>/', SensorRetrieveView.as_view(), name='sensor-retrieve'),
    path('measurements/create/', MeasurementCreateView.as_view(), name='measurement-create'),
]
