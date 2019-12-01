import math

def is_powed(a, b, c):
   p = (a+b+c) / 2
   return math.sqrt(p*(p-a)*(p-b)*(p-c))

a = float(input())
b = float(input())
c = float(input())

S = is_powed(a, b, c)
print(S)