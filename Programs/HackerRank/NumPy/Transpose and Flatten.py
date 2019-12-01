# Transpose
#
# We can generate the transposition of an array using the tool numpy.transpose.
# It will not affect the original array, but it will create a new array.
#
# import numpy
#
# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print numpy.transpose(my_array)
#
# #Output
# [[1 4]
#  [2 5]
#  [3 6]]
# Flatten
#
# The tool flatten creates a copy of the input array flattened to one dimension.
#
# import numpy
#
# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print my_array.flatten()
#
# #Output
# [1 2 3 4 5 6]

# Sample Input
#
# 2 2
# 1 2
# 3 4
# Sample Output
#
# [[1 3]
#  [2 4]]
# [1 2 3 4]

import numpy as np

n, m = map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)
print(array.T)
print(array.flatten())
