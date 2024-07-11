def binary(n):
    if n > 1:
        binary(n // 2)
    print(n % 2, end='')

t = int(input())
a = []
for _ in range(t):
    num = int(input())
    a.append(num)
print()
for num in a:
    binary(num)
    print()