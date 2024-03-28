"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from measurement.views import SensorListCreateView
from measurement.views import SensorCreateView, SensorListView, SensorUpdateView, MeasurementCreateView, SensorRetrieveView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),
    path('home/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('sensors/create/', SensorCreateView.as_view(), name='sensor-create'),
    path('sensors/<int:pk>/', SensorUpdateView.as_view(), name='sensor-update'),
    path('sensors/<int:pk>/', SensorRetrieveView.as_view(), name='sensor-retrieve'),
    path('measurements/create/', MeasurementCreateView.as_view(), name='measurement-create'),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('measurement.urls')), # -- не знаю почему, но маршруты не работают, прописал в ручную--
#     path('home/', SensorListCreateView.as_view(), name='sensor-list-create'),
#     path('sensors/', SensorListView.as_view(), name='sensor-list'),
#     path('sensors/create/', SensorCreateView.as_view(), name='sensor-create'),
#     path('sensors/<int:pk>/', SensorUpdateView.as_view(), name='sensor-update'),
#     path('sensors/<int:pk>/', SensorRetrieveView.as_view(), name='sensor-retrieve'),
#     path('measurements/create/', MeasurementCreateView.as_view(), name='measurement-create'),
# ]
