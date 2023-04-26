from django.shortcuts import render, HttpResponse
from apiapp.models import Student
from apiapp.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
 

# Create your views here.

def student_detail(request,val):
    stud=Student.objects.get(id=val)
    serializer=StudentSerializer(stud)
    
    json_data=JSONRenderer().render(serializer.data)
    print(type(json_data))
     
    return HttpResponse(json_data, content_type="application/json")

# queryset data
def student_list(request):
    stud=Student.objects.all()
    serializer=StudentSerializer(stud, many=True)
 
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
     
    return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        serializer= StudentSerializer(data=pydata)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")

        json_data=JSONRenderer(json_data, content_type='application/json')