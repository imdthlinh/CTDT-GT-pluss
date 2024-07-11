def timSoLonNhat(n):
    if n == 0:
        return 0

    max = timSoLonNhat(int(n/10))
    if (n % 10 < max):
        return max

    return (n % 10)

t = int(input())

while(t):
    n = int(input())
    print(n ,': ', timSoLonNhat(n), sep='')
    t -= 1