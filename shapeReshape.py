import numpy as np

inp = list(map(int, input().split()))
nparr = np.array(inp)
print(nparr.reshape(3,3))