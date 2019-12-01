# dot
#
# The dot tool returns the dot product of two arrays.
#
# import numpy
#
# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])
#
# print numpy.dot(A, B)       #Output : 11
# cross
#
# The cross tool returns the cross product of two arrays.
#
# import numpy
#
# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])
#
# print numpy.cross(A, B)     #Output : -2

# Sample Input
#
# 2
# 1 2
# 3 4
# 1 2
# 3 4
# Sample Output
#
# [[ 7 10]
#  [15 22]]

import numpy as np

a = int(input())

A = np.array([input().split() for _ in range(a)]).astype(int)
B = np.array([input().split() for _ in range(a)]).astype(int)

print(A, B, sep='\n')
print(np.dot(A, B))
