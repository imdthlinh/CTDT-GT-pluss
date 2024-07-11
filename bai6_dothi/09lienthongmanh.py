MAX_NODES = 100

n = 0 #Số đỉnh
# Ma trận kề biểu diễn đồ thị với giá trị ban đầu là 0
G = [[0 for _ in range(MAX_NODES)] for _ in range(MAX_NODES)]
# đánh dấu các đỉnh đã được thăm
visited = [0] * MAX_NODES
# lưu thứ tự các đỉnh
order = [0] * MAX_NODES
# đếm số lượng đỉnh đã được thăm
count = 0

def dfs1(u): #tìm thứ tự các đỉnh
    global count
    visited[u] = 1
    for v in range(n):
        # Nếu có cạnh nối từ u đến v và đỉnh v chưa được thăm
        if G[u][v] and not visited[v]:
            dfs1(v)
    order[count] = u
    count += 1

def dfs2(u): #duyệt đồ thị chuyển vị
    visited[u] = 1
    for v in range(n):
        if G[v][u] and not visited[v]:
            dfs2(v)

def is_strongly_connected():
    global count
    count = 0
    # Đặt lại danh sách chưa thăm
    for u in range(n):
        visited[u] = 0
    # tìm thứ tự các đỉnh
    for u in range(n):
        if not visited[u]:
            dfs1(u)

    # Đặt lại danh sách chưa thăm
    for u in range(n):
        visited[u] = 0
    scc_count = 0  # đếm số lượng thành phần liên thông mạnh
    # chuyển vị theo thứ tự ngược lại
    for i in range(count - 1, -1, -1):
        u = order[i]
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    return scc_count == 1 #đồ thị liên thông mạnh

t = int(input())
while t > 0:
    n = int(input())
    for u in range(n):
        row = list(map(int, input().split()))
        for v in range(n):
            G[u][v] = row[v]
    if is_strongly_connected():
        print("Strongly Connected")
    else:
        print("Not connected")
    t -= 1