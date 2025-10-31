import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3], [4,5,6]])
arr3 = np.array([[[1,2],[3,4],[5,6]]])

print(arr1.ndim, "D")
print(arr2.ndim, "D")
print(arr3.ndim, "D")
