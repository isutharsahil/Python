import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[0]) # first element
print(arr[-1]) # last element

# slicing  [start: stop: step]
print(arr[0:3]) 
print(arr[::-1]) #reverse
print(arr[::2]) #every second element