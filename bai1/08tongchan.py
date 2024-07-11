#loi
def tong_chan(n, a):
    if n == 0:
        return 0
    else:
        if a[n - 1] % 2 == 0:
            return tong_chan(n - 1, a) + a[n - 1]
    return tong_chan(n-1, a)

n = (int)(input())
input_line = input().split(' ')
a = [int(x) for x in input_line]
print(tong_chan(n, a))