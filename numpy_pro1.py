import numpy as np

arr = np.array([1, 2, 3, 4, 5,6])
print(arr)
print(arr.ndim)
print(arr[2])
print(arr[1:3])
print(arr.shape)
arr.reshape(3, 2)
print(arr)
newarr = np.array_split(arr, 3)

print(newarr)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.ndim)
print(arr2[1][1])
print(np.sort(arr2))


arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)
print(arr3.ndim)
print(arr3[1][1][1])

