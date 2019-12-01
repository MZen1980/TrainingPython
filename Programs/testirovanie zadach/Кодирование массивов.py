import numpy as np


def encode(a):
    count = 0
    a_encode = []
    a_count_el = []

    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count += 1
        else:
            count += 1
            a_encode.append(a[i])
            a_count_el.append(count)
            count = 0

    count += 1
    a_encode.append(a[i])
    a_count_el.append(count)
    count = 0
    out = (a_encode, a_count_el)

    return out


arr = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])

en = encode(arr)
# print(en)
# = (np.array([1, 2, 3, 1, 5, 2, 3]), np.array([1, 2, 2, 2, 2, 1, 2])))
