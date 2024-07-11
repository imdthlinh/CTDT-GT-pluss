def tinh_XY(n):
    X = [0] * (n + 1)
    Y = [0] * (n + 1)

    X[0] = 1
    Y[0] = 0

    for i in range(1, n + 1):
        X[i] = X[i - 1] + Y[i - 1]
        Y[i] = 3 * X[i - 1] + Y[i - 1]

    return X, Y

t = int(input())
results = []
 
for _ in range(t):
    n = int(input())
    x, y = tinh_XY(n)
    results.append((x[n], y[n]))

for result in results:
    print(f"{result[0]} {result[1]}")


