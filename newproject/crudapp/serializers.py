from rest_framework import serializers
from crudapp.models import Employee

class EmployeeSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    desg=serializers.CharField(max_length=200)
    age=serializers.IntegerField()
    doj=serializers.DateField(format="%d-%m-%Y")
    # other way to implement :
    # class meta:
    #     modal=Employee
    #     fields="__all__"

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name=validate_data.get('name', instance.name)
        instance.desg=validate_data.get('desg', instance.desg)
        instance.age=validate_data.get('age', instance.age)
        instance.doj=validate_data.get('Doj', instance.doj)

        instance.save()
        return instance
