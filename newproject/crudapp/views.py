from django.shortcuts import render, HttpResponse
from crudapp.models import Employee
from crudapp.serializers import EmployeeSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie 
 

# Create your views here.
def employee_detail(request, val):
    emp=Employee.objects.get(id=val)
    serializer=EmployeeSerializers(emp)
    j_data=JSONRenderer().render(serializer.data)

    return HttpResponse(j_data, content_type='application/json')

# @ensure_csrf_cookie 
@csrf_exempt
def employee_api(request):
    if request.method=='GET':
        j_data=request.body
        stream=io.BytesIO(j_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id', None)
        # id=pydata.get['id']
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer=EmployeeSerializers(emp)
            # j_data=JSONRenderer().render(serializer.data)
            # return HttpResponse(j_data, content_type='application/json')
            return JsonResponse(serializer.data, safe=False)
        
        emp = Employee.objects.all()
        serializer=EmployeeSerializers(emp, many=True)
        # j_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(j_data, content_type='application/json')
        # return JsonResponse({'data':j_data})
        return JsonResponse(serializer.data, safe=False)

    if request.method=='POST':
        j_data=request.body
        stream=io.BytesIO(j_data)
        pydata=JSONParser().parse(stream)
        serializer=EmployeeSerializers(data=pydata)

        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data Inserted Succesfully...."}
            return JsonResponse(res)
            # jdata = JSONRenderer().render(res)
            # return HttpResponse(jdata, content_type='application/json')
        # If not valid
        # jdata = JSONRenderer().render(serializer.errors)
        # print(jdata)
        return JsonResponse(serializer.errors)
        # return HttpResponse(jdata, content_type='application/json')
          
    if request.method=='PUT':
        j_data=request.body
        stream = io.BytesIO(j_data)
        pydata=JSONParser().parse(stream)      
        id=pydata.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializers(emp, data=pydata, partial=True)

        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data Updated Succesfully...."}
            # jdata=JSONRenderer().render(res)
            return JsonResponse(res)
        
        return JsonResponse(serializer.errors)
    
    if request.method=='DELETE':
        j_data=request.body
        stream=io.BytesIO(j_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        emp=Employee.objects.get(id=id)
        # if emp is not None:
        emp.delete()
        res={'msg':"Data Deleted Succesfully...."}
        jdata = JSONRenderer().render(res)
        return HttpResponse(jdata,content_type='application/json')
        # return JsonResponse({'res':'Data not found!!!'})
    
     