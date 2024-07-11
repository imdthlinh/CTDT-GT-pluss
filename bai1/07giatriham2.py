def giaTriHam2(i, n):
    if i == n:
        return n ** 0.5
    else:
        return (i + giaTriHam2(i + 1, n)) ** 0.5

t = int(input())
count = 0
while count < t:
    n = int(input())
    print("{:.10f}".format(giaTriHam2(1, n)))
    count += 1