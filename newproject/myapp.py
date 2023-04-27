import requests
import json

# url= "http://localhost:8000/studentlist"

'''r=requests.get(url='http://localhost:8000/studentcreate')

data=r.json()

print(data)'''
# --------------------------------------------------------------------------

# insert data:

# data = {
#     'roll':101,
#     'name':'mahi',
#     'city':'indore',
#     'age':20
# }

# json_data=json.dumps(data)

# r=requests.post(url='http://localhost:8000/studentcreate/', data=json_data)

# data=r.json()
# print(data)

# --------------------------------------------------------------------------

def get_data(id= None):
    data={}
    if id is not None:
        data={'id':id}
    j_data=json.dumps(data) #convert to json

    r=requests.get(url = "http://localhost:8000/employeeinfo/", data=j_data)
    data=r.json()
    print(data)


def post_data():
    data={'name':'jayesh','desg':"HR",'age':20,'doj':'2023-03-05'}

    json_data=json.dumps(data)
    res=requests.post(url='http://localhost:8000/employeeinfo/', data=json_data)
    data=res.json()
    print(data)

def put_data():
    data={'id': 9, 'name': 'manshi', 'age':12}
    json_data=json.dumps(data)
    res=requests.put(url='http://localhost:8000/employeeinfo/', data=json_data)
    data=res.json()
    print(data)

def delete_data():
    data={'id':3}
    j_data=json.dumps(data)
    res=requests.delete(url="http://localhost:8000/employeeinfo/", data=j_data)
    data=res.json()
    print(data)    


get_data(2)
# post_data()
# put_data()
# delete_data()