import numpy as np

def no_numpy_scalar(v1, v2):
    #YOUR CODE: please do not use numpy
    a = v1
    b = v2
    # s = 0  # сумма
    # t = []  # временная матрица
    # m3 = []  # конечная матрица
    # if len(m2) != len(m1[0]):
    #     print("Матрицы не могут быть перемножены")
    # else:
    #     r1 = len(m1)  # количество строк в первой матрице
    #     c1 = len(m1[0])  # Количество столбцов в 1
    #     r2 = c1  # и строк во 2ой матрице
    #     c2 = len(m2[0])  # количество столбцов во 2ой матрице
    #     for z in range(0, r1):
    #         for j in range(0, c2):
    #             for i in range(0, c1):
    #                 s = s + m1[z][i] * m2[i][j]
    #             t.append(s)
    #             s = 0
    #         m3.append(t)
    #         t = []
    #     return m3
    return sum([a[i]*b[i] for i in range(len(a))])

def numpy_scalar (v1, v2):
    #YOUR CODE

    result = np.dot(v1, v2)
    return result

v1 = [1, 5, 5]
v2 = [1, 6, 6]
test = no_numpy_scalar(v1, v2)
print(test)
assert test == 61, ('Неверный результат в no_numpy_scalar')

v1 = np.array([1, 5, 5])
v2 = np.array([1, 6, 6])
x1 = numpy_scalar(v1, v2)
x2 = 61
assert np.array_equal(x1, x2) , ('Неверный результат в numpy_scalar')