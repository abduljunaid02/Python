import numpy as np

n,m,p = map(int, input().split())

arr1 = np.array([input().split() for i in range(n)],int)
arr2 = np.array([input().split() for i in range(m)], int)
con = np.concatenate((arr1, arr2), axis=1)
print(con)
print(con.shape)