import numpy as np
n,m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
print(arr)
sum1 = np.sum(arr, axis=0)
print(np.prod(sum1))