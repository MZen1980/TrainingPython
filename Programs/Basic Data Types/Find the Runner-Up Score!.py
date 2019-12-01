# a = input()
# b = ([int(i) for i in input().split()])
# max_b = max(b)
# min_b = min(b)
# c = min_b
# for x in b:
#     if c < x < max_b:
#         c = x
# print(x)


# print(b)

# n = int(input())
# arr = map(int, input().split())

n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
i = 0
while (i < n):
    if zes == max(arr):
        arr.remove(max(arr))
    i += 1
print(max(arr))
