from rest_framework import serializers
from .models import Iot

class IotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Iot
        fields=('title', 'gps_x', 'gps_y', 'time_create', 'param_value')