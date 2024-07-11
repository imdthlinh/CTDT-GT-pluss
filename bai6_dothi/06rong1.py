from collections import deque

def bfs(visited, index, arr, n):
	#visited: danh sách đánh dấu các đỉnh đã được thăm
	#index: chỉ số của đỉnh ban đầu
	#arr: ma trận kề của đồ thị
	#n: số lượng đỉnh trong đồ thị
    q = deque()  # Khởi tạo hàng đợi để lưu trữ các đỉnh sẽ được duyệt
    q.append(index)  
    visited[index] = 1  
    while q:
        v = q.popleft()  # Lấy đỉnh đầu tiên ra khỏi hàng đợi
        for i in range(n):
            # Duyệt qua các đỉnh chưa được thăm. Nếu chưa thăm, thêm vào hàng đợi và đánh dấu là đã thăm
            if arr[v][i] == 1 and index != i and visited[i] == 0:
                q.append(i)  
                visited[i] = 1  

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        
        arr = [list(map(int, input().split())) for _ in range(n)]  # Đọc ma trận kề của đồ thị

        for i in range(n):
            visited = [0] * n  # Khởi tạo danh sách đánh dấu các đỉnh chưa được thăm
            first = 1  # biến cờ

            # Đánh dấu hàng đã được thăm
            bfs(visited, i, arr, n)

            print(f"From{i:4d} can visit:", end=" ")

            for j in range(n):
                # Nếu kết quả từ BFS là True => có thể thăm được
                if j != i and visited[j] == 1:
                    # Nếu là số đầu tiên, không in dấu phẩy
                    if first == 1:
                        first = 0
                    else:
                        print(",", end="")
                    print(f"{j:3d}", end="")

            # Trong trường hợp không có đỉnh nào được kết nối
            if first == 1:
                print("No vertex", end="")

            print()

        print()

if __name__ == "__main__":
    main()