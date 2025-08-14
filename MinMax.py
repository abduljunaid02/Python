import numpy as np

n,m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

print(np.min(arr, axis=1))