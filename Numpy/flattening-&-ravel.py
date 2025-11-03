# .ravel() -> views (modify original data)
# .flatten() -> copy 
# use-case = For converting multi dimension array into a 1D array.
import numpy as np

arr_2d = np.array([[1,2,3], [4,5,6]])

print(arr_2d.ravel())
print(arr_2d.flatten())