import numpy as np

n = int(input())

arr1 = np.array([input().split() for _ in range(n)],dtype=int)
arr2 = np.array([input().split() for _ in range(n)],dtype=int)
print(np.dot(arr1, arr2))
print(np.cross(arr1, arr2))