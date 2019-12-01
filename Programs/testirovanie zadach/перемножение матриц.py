import numpy as np


def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param first: list of "size" lists, each contains "size" floats
    """
    m1 = first
    m2 = second
    s = 0  # сумма
    t = []  # временная матрица
    m3 = []  # конечная матрица
    if len(second) != len(first[0]):
        print("Матрицы не могут быть перемножены")
    else:
        r1 = len(m1)  # количество строк в первой матрице
        c1 = len(m1[0])  # Количество столбцов в 1
        r2 = c1  # и строк во 2ой матрице
        c2 = len(m2[0])  # количество столбцов во 2ой матрице
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + m1[z][i] * m2[i][j]
                t.append(s)
                s = 0
            m3.append(t)
            t = []
        return m3


def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """
    # YOUR CODE: please use numpy

    result = np.dot(first, second)
    return result


first = [[1, 5, 5], [4, 1, 4], [3, 3, 1]]
second = [[1, 6, 6], [7, 1, 7], [8, 8, 1]]
test1 = no_numpy_mult(first, second)
print(test1)
# test2 = numpy_mult(first, second)
# print(test2)
# assert test2 == [[76, 51, 46], [43, 57, 35], [32, 29, 40]] #, ('Неверный результат в no_numpy_mult')
