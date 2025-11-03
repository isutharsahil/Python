# loop's next gen

import numpy as np

prices = np.array([100,200,300])
discount = 10

final = prices - (prices * discount/100)

print(final)