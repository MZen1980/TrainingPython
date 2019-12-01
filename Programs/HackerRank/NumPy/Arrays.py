# import numpy
#
# a = numpy.array([1,2,3,4,5])
# print a[1]          #2
#
# b = numpy.array([1,2,3,4,5],float)
# print b[1]          #2.0
#
# Sample Input
#
# 1 2 3 4 -8 -10
# Sample Output
#
# [-10.  -8.   4.   3.   2.   1.]

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr, dtype=numpy.float64)
    return a[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)