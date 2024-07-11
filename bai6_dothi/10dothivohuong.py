import numpy as np

MAX_N = 100

#chuyển đồ thị thành đồ thị vô hướng
def make_undirected_graph(a):
    # Lấy kích thước của ma trận a (n x n)
    n = a.shape[0]
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                a[j][i] = a[i][j]
    return a

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        # Khởi tạo ma trận a
        a = np.zeros((n, n), dtype=int)
        for i in range(n):
            a[i] = list(map(int, input().split()))
        a = make_undirected_graph(a)
        for row in a:
            print(" ".join(map(str, row)))
        print()
        t -= 1 

if __name__ == "__main__":
    main()