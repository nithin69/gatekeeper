from rest_framework import serializers

from nh5.models import (
    Employee,
)



class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'phone')
