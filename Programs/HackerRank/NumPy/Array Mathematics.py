# Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.
#
# import numpy
#
# a = numpy.array([1,2,3,4], float)
# b = numpy.array([5,6,7,8], float)
#
# print a + b                     #[  6.   8.  10.  12.]
# print numpy.add(a, b)           #[  6.   8.  10.  12.]   # сложение
#
# print a - b                     #[-4. -4. -4. -4.]
# print numpy.subtract(a, b)      #[-4. -4. -4. -4.]       # вычитание
#
# print a * b                     #[  5.  12.  21.  32.]
# print numpy.multiply(a, b)      #[  5.  12.  21.  32.]   # умножение
#
# print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
# print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]  # деление
#
# print a % b                     #[ 1.  2.  3.  4.]
# print numpy.mod(a, b)           #[ 1.  2.  3.  4.]  # остаток от деления
#
# print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
# print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04] # возведение в степень

# Sample Input
#
# 1 4
# 1 2 3 4
# 5 6 7 8
# Sample Output
#
# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]]

import numpy as np

a, b = map(int, input().split())

arr1, arr2 = (np.array([input().split() for _ in range(a)], dtype=np.int) for _ in range(2))

print(np.add(arr1, arr2),
      np.subtract(arr1, arr2),
      np.multiply(arr1, arr2),
      np.divide(arr1, arr2).astype(int),  # преобразуем в тип целое число
      np.mod(arr1, arr2),
      np.power(arr1, arr2),
      sep='\n'
      )
# arr2 = np.array([input().split() for _ in range(2)], dtype=np.int)

# print(np.add(arr1, arr2))
