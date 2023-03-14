from rest_framework import serializers
from employee.models import Employee


# Register Serializer Class and defined Model and Fields
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
