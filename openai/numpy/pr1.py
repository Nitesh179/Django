import numpy as np

'''arr=np.array([1,2,3,4])
print(arr)

arrv=np.array([[1],[2],[3],[4]])

print(arrv)'''

# arr=np.array([(1,2,3),(4,5,6)])
# print(arr)

# arr=np.arange(0,10,2)
# print(arr)

# arr=np.linspace(0,5,9)
# print(arr)

# arr=np.random.rand(2,3)*255
# print(arr)

# arr=np.array([(1,2,3),(4,5,6)])
# arr1=np.array([(4,5,6),(1,2,3)])
# print(arr+arr1)

arr=np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6]])

print(arr.reshape(2,9))