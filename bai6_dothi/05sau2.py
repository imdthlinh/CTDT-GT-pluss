def dfs(visited, index, arr, n, parents): #hàm dfs để thực hiện tìm kiếm theo chiều sâu
#visited: danh sách đánh dấu các đỉnh đã được thăm
#index: chỉ số của đỉnh hiện tại
#arr: ma trận kề của đồ thị
#n: số đỉnh của đồ thị
#parents: danh sách lưu trữ cha của mỗi đỉnh trong cây DFS
    visited[index] = 1 #đánh dấu đỉnh index đã được thăm
    for i in range(n):
        #Nếu có cạnh kề giữa đỉnh index và đỉnh i (arr[index][i] == 1)
        #index khác i, và đỉnh i chưa được thăm (visited[i] == 0)
        if arr[index][i] == 1 and index != i and visited[i] == 0:
            parents[i] = index #Gán index làm cha của i
            dfs(visited, i, arr, n, parents)

def main():
    t = int(input())
    for _ in range(t):
        #n là số đỉnh của đồ thị, u là đỉnh bắt đầu, và v là đỉnh kết thúc
        n, u, v = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(n)]
        visited = [0] * n
        parents = [-1] * n
        dfs(visited, u, arr, n, parents)

        print(f"Path from {u} to {v}:", end=" ")
        if visited[v] == 0:
            print("No path exits")
        else:
            path = [] #danh sách path để lưu trữ đường đi từ u đến v
            tmp = v
            while u != tmp:
                path.append(tmp)
                tmp = parents[tmp]
            path.append(u)
            print(" --> ".join(map(str, reversed(path))))

if __name__ == "__main__":
    main()