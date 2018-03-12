from rest_framework import serializers
from gatekeeperapp.models import *

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
