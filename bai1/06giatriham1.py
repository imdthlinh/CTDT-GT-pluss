import math

def giaTriHam(n):
    if n == 1:
        return 1
    return math.sqrt(n + giaTriHam(n-1))

t = int(input())
a = []

for i in range(0, t):
    a.append(int(input()))

for element in a:
    print("{:.10f}".format(giaTriHam(element)))

   