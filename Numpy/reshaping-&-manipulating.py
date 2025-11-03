# Reshape => changing shape/dimensions of an array without modifying array's data
# reshape(rows, columns) specify new shape
# it reshapes only if dimensions matches

import numpy as np

arr = np.array([1,2,3,4,5,6])
reshape_arr = arr.reshape(3,2)
print(reshape_arr)