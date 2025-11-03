# vertically       - horizontally
# vstack() 'row'   - hstack()  "column"

import numpy as np

arr = np.array([1,2,3])
arr2 = np.array([4,5,6])
print("vertical stack",np.vstack((arr, arr2))) # vstack
print("Horizonatal stack",np.hstack((arr, arr2))) # hstack
print("\n \n")
# equal and normal split = np.split(array, parts/splits)
# verticall split = np.vsplit()
# horizontal split  = np.hsplit()

varr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("split", np.split(varr, 6))
# print("vsplit", np.vsplit(varr, 3)) # for more than one dimension
# print("hsplit", np.hsplit(varr, 1)) # for more than one dimension
