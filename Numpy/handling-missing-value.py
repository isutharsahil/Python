# builtin function isnan -> nan is stands for Not a number.
# np.isnan(array)

import numpy as np

arr = np.array([1,2,np.nan, 4, np.nan, 6])

print(np.isnan(arr))
print(np.nan == np.nan) # can not compare it directly

# putting a number in missing numbers
cleaned_arr = np.nan_to_num(arr,nan=100)
print(cleaned_arr)


# isnf(array)
arr1 = np.array([1,2,np.nan, 4, -np.nan, 6])
print(np.isinf(arr1))
