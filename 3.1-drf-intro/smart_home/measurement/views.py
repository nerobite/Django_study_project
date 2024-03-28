# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Sensor
from .serializers import SensorDetailSerializer
from .models import Measurement
from .serializers import MeasurementSerializer

class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorCreateView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorRetrieveView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer