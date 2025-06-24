import numpy as np
n, m = map(int,input().split())
arr = np.array([input().split() for i in range(n)], int)
print(np.transpose(arr))
print(arr.flatten())


# list comprehension - returns a list
#split() used with input when there are more than one inputs like n,m or do list(...)