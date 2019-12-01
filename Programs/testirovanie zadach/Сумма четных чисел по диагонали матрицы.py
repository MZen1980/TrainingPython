import numpy as np


def diag_2k(b):
    a = np.asarray(b).astype(int)
    sum = 0
    l = np.diagonal(a)
    for i in range(len(l)):
        if l[i] % 2 == 0:
            sum += (l[i])

    result = sum
    return result


arr = np.array([
    [4, 6, 1, 5, 5],
    [9, 2, 6, 7, 4],
    [9, 2, 8, 3, 7],
    [7, 6, 2, 4, 7],
    [5, 9, 7, 6, 9]
])

n = diag_2k(arr)
print(n)
