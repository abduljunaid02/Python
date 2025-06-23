import numpy as np

inp = map(int, input().split())
arr = []
for num in inp:
    arr.append(num)
print(arr)
nparr = np.array(arr)
print(nparr.shape)
print(nparr.reshape(3,3))