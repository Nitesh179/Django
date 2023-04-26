import requests
import json

url= "http://localhost:8000/studentlist"

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

def post_data():
    data={
        'name':'jayesh',
        'desg':"HR",
        'age':20,
        'Doj':'23/03/2023'
    }

    json_data=json.dumps(data)
    res=requests.post(url='http://localhost:8000/', data=json_data)
    data=res.json()
    print(data)

def post_data():
    data={
        'name':'jayesh',
        'desg':"HR"
    }

    json_data=json.dumps(data)
    res=requests.put(url='http://localhost:8000/', data=json_data)
    data=res.json()
    print(data)
