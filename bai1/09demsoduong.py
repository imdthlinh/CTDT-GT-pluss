def count_Positive(n, a):
    if n == 0:
        return 0
    else:
        if a[n - 1] > 0:
            return count_Positive(n - 1, a) + 1
    return count_Positive(n - 1, a)

n = int(input())
a = list(map(float, input().split()))

count = count_Positive(n, a)

print(count)


