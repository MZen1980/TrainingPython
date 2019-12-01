# inner
#
# The inner tool returns the inner product of two arrays.
#
# import numpy
#
# A = numpy.array([0, 1])
# B = numpy.array([3, 4])
#
# print numpy.inner(A, B)     #Output : 4
# outer
#
# The outer tool returns the outer product of two arrays.
#
# import numpy
#
# A = numpy.array([0, 1])
# B = numpy.array([3, 4])
#
# print numpy.outer(A, B)     #Output : [[0 0]
#                             #          [3 4]]
#
# Sample Input
#
# 0 1
# 2 3
# Sample Output
#
# 3
# [[0 0]
#  [2 3]]

import numpy as np

A = np.array([input().split()]).astype(int)
B = np.array([input().split()], dtype=np.int)

print(int(np.inner(A, B)))
print(np.outer(A, B))
