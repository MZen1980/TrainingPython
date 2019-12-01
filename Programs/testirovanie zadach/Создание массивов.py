def cumsum_and_erase(A, erase: int = 1):
    b = list()
    for i in A:
        if i != erase:
            b.append(i)
        else:
            continue

    B = b
    return B



# a = [1, 1, 1, 4, 5, 6, 7, 8, 9, 10]
# с = cumsum_and_erase(a, 1)
# print(с)

def Test():
    tests = [[[1, 2, 3, 4, 5, 6], 1], [[4, 2, 5, 1, 3, 2], 5], [[3, 3, 3, 3, 3, 4], 15]]
    result_test = [[3, 6, 10, 15, 21], [4, 6, 11, 12, 15, 17], [3, 6, 9, 12, 19]]
    result = True
    for i in range(len(tests)):
        result = result and (cumsum_and_erase(tests[i][0], tests[i][1]) == result_test[i])
    if result:
        print("Задание успешно выполнено!")
    else:
        print("Ошибка в решении!")


Test()
