# this function is for joining multiple arrays together.
# np.concatenate(array1, array2, .....n)

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])

new  = np.concatenate((arr1, arr2, arr3))
print(new)