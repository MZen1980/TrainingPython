N = int(input())


def factor(x):
    if x == 1:
        return x
    elif x % 2 == 0:
        return factor(x-1)
    else:
        return x * factor(x - 1)


N_double_fact = factor(N)

print(N_double_fact)
