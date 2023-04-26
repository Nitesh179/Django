from rest_framework import serializers
from apiapp.models import Student

class StudentSerializer(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=100)
    age=serializers.IntegerField()
    

    def create(self, validate_data):
        return Student.objects.create(**validate_data)    
    
    


#  more serializers fields:

# '''
# -> label
# -> required

# -> charField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
# -> Boolean Fields
# -> String Fields
# -> Numeric Fields
# -> Date and Time Fields
# -> Choice Selection Fields
# -> File Upload Fields
# -> Serializer Fields
# -> Core arguments in serializer fields 
#    -> password = serializers.CharField(max_length=100, style={'input_type': 'password', 'placeholder': 'enter password'})
# '''