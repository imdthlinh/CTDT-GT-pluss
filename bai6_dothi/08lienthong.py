def dfs(a, visited, u):
    #a: ma trận kề của đồ thị
    #visited: danh sách đánh dấu các đỉnh đã được thăm
    #u: chỉ số của đỉnh hiện tại đang được duyệt
    visited[u] = 1

    for v in range(len(a)):
        # Nếu có cạnh nối từ đỉnh u đến v và đỉnh v chưa được thăm
        if a[u][v] and not visited[v]:
            dfs(a, visited, v)

def is_connected(a, n):
    visited = [0] * n
    
    # Bắt đầu duyệt đồ thị từ đỉnh 0
    dfs(a, visited, 0)
    
    # Kiểm tra tất cả các đỉnh trong đồ thị
    for u in range(n):
        if not visited[u]:
            return 0
    
    return 1

def main():
    t = int(input())
    
    while t > 0:
        n = int(input())
        
        a = []
        
        # Đọc từng hàng của ma trận kề từ đầu vào và thêm vào danh sách a
        for i in range(n):
            row = list(map(int, input().split()))
            a.append(row)
        
        if is_connected(a, n):
            print("Connected")
        else:
            print("Not connected")
        
        t -= 1

if __name__ == "__main__":
    main()
