def hoan_vi(i):
    if i == n:
        print(*a)
        return
    for j in range(n, 0, -1):
        if not check[j]:
            check[j] = True
            a[i] = j
            hoan_vi(i+1)
            check[j] = False

n=int(input())
a = [0] * n
check = [False] * (n+1)

hoan_vi(0)