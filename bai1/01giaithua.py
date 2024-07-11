import math

n = int(input())
def giaiThua(n):
    if n == 0:
        print("{}! = {}".format(n,1))
        return 1

    a = n * giaiThua(n - 1)

    print("{}! = {}".format(n,a))

    return a
  
giaiThua(n)
    