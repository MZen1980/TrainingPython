# mean
#
# The mean tool computes the arithmetic mean along the specified axis.
#
# import numpy
#
# my_array = numpy.array([ [1, 2], [3, 4] ])
#
# print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
# print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
# print numpy.mean(my_array, axis = None)     #Output : 2.5
# print numpy.mean(my_array)                  #Output : 2.5
# By default, the axis is None. Therefore, it computes the mean of the flattened array.
#
# var
#
# The var tool computes the arithmetic variance along the specified axis.
#
# import numpy
#
# my_array = numpy.array([ [1, 2], [3, 4] ])
#
# print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
# print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
# print numpy.var(my_array, axis = None)      #Output : 1.25
# print numpy.var(my_array)                   #Output : 1.25
# By default, the axis is None. Therefore, it computes the variance of the flattened array.
#
# std
#
# The std tool computes the arithmetic standard deviation along the specified axis.
#
# import numpy
#
# my_array = numpy.array([ [1, 2], [3, 4] ])
#
# print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
# print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
# print numpy.std(my_array, axis = None)      #Output : 1.11803398875
# print numpy.std(my_array)                   #Output : 1.11803398875
# By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.

# Sample Input
#
# 2 2
# 1 2
# 3 4
# Sample Output
#
# [ 1.5  3.5]
# [ 1.  1.]
# 1.11803398875

import numpy as np

a, b = map(int, input().split())
arr = np.array([input().split() for _ in range(a)], dtype=np.int)
# print(str(arr.mean(axis=1)).replace(' ', '  ').replace('[', '[ '))
# print(str(arr.var(axis=0)).replace(' ', '  ').replace('[', '[ '))
# print(round(arr.std(axis=None), 11))

np.set_printoptions(legacy='1.13')
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.std(arr))