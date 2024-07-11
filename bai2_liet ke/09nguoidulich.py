def nhap(): #Đọc vào số lượng thành phố và ma trận chi phí c. Đồng thời tìm chi phí nhỏ nhất cmin trong ma trận.
    global n, c, cmin
    n = int(input())
    c = []
    cmin = float('inf')

    for i in range(n):
        row = list(map(int, input().split()))
        c.append(row)
        for j in range(n):
            if row[j] != 0:
                cmin = min(cmin, row[j])

def Try(i): #Hàm đệ quy để thử tất cả các đường đi có thể, cập nhật d và ktra xem có thể cập nhật ans ko
    global d, ans #d: chi phí, ans: kết quả
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            X[i] = j
            d += c[X[i-1]][X[i]]
            if i == n - 1:
                ans = min(ans, d + c[X[n-1]][X[0]])
            elif d + (n - i - 1) * cmin < ans:
                Try(i + 1)
            visited[j] = False
            d -= c[X[i-1]][X[i]]

if __name__ == "__main__":
    n = 0
    c = []
    X = []
    visited = []
    d = 0
    ans = float('inf')
    cmin = float('inf')

    nhap()
    X = [0] * n
    visited = [False] * n
    X[0] = 0
    visited[0] = True
    Try(1)
    print(ans)