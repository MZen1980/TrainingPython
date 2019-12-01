# floor
# The tool floor returns the floor of the input element-wise.
# The floor of  is the largest integer  where .
#
# import numpy
#
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# ceil
# The tool ceil returns the ceiling of the input element-wise.
# The ceiling of  is the smallest integer  where .
#
# import numpy
#
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# rint
# The rint tool rounds to the nearest integer of input element-wise.
#
# import numpy
#
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

# Sample Input
#
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
# Sample Output
#
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]

import numpy as np

a = input().strip().split(' ')
# my_array = np.array(a, dtype= np.float64) # преобразовать тип можно так или
my_array = np.array(a).astype(float)  # так
# print(my_array)
print(str(np.floor(my_array)).replace('.', '. ').replace('[', '[ ').replace(' ]', ']'))
print(str(np.ceil(my_array)).replace('.', '. ').replace('[', '[ ').replace(' ]', ']'))
print(str(np.rint(my_array)).replace('.', '. ').replace('[', '[ ').replace(' ]', ']'))
