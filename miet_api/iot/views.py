from django.forms import model_to_dict
from .models import Iot
from .serializers import IotSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets


class IotViewSet(viewsets.ModelViewSet):
    queryset=Iot.objects.all()
    serializer_class=IotSerializer





# # get, post 
# class IotAPIList(generics.ListCreateAPIView):
#     queryset=Iot.objects.all()
#     serializer_class=IotSerializer

# # put, patch
# class IotAPIUpdate(generics.UpdateAPIView):
#     queryset=Iot.objects.all()
#     serializer_class=IotSerializer

# # изменить и удалить конкретную запись
# class IotAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Iot.objects.all()
#     serializer_class=IotSerializer
