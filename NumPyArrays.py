import numpy

def arrays(arr):
    a = [i for i in reversed(arr)]
    b = numpy.array(a, float)
    return b 
arr = input().strip().split(' ')
result = arrays(arr)
print(result)