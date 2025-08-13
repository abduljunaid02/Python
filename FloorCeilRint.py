import numpy as np
np.set_printoptions(legacy="1.13")
x = np.array([1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9])
x = np.array(input().split(), float)
print(np.floor(x))
print(np.ceil(x))
print(np.rint(x))