import numpy as np

dim = tuple(map(int, input().split()))
Adata = list(map(int, input().split()))
A = np.array(Adata).reshape(dim)
Bdata = list(map(int, input().split()))
B = np.array(Bdata).reshape(dim)



print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(np.floor_divide(A,B))
print(np.mod(A,B))
print(np.power(A,B))
