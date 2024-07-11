def dfs(visited, index, arr, n, arrIndex, indexStack):
    visited[index] = 1 
    arrIndex.append(index)  # Thêm đỉnh hiện tại vào danh sách duyệt theo chiều sâu
    for i in range(n):
        # Nếu có cạnh nối từ đỉnh hiện tại đến đỉnh i và đỉnh i chưa được duyệt
        if arr[index][i] == 1 and index != i and visited[i] == 0:
            dfs(visited, i, arr, n, arrIndex, indexStack)

def dfs1(visited, index, arr, n):
    visited[index] = 1
    for i in range(n):  # Duyệt qua mỗi đỉnh
        # Nếu có cạnh nối và đỉnh i chưa được duyệt
        if arr[index][i] == 1 and index != i and visited[i] == 0:
            dfs1(visited, i, arr, n)  # Duyệt tiếp từ đỉnh i

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        arrTG = []  # Ma trận kề của đồ thị chuyển vị
        arrVH = []  # Ma trận kề của đồ thị vô hướng
        # Khởi tạo ma trận kề cho arr, arrTG, arrVH
        for i in range(n):
            arr.append(list(map(int, input().split())))
            arrTG.append([0] * n)
            arrVH.append([0] * n)

        for i in range(n):
            for j in range(n):
                arrVH[i][j] = arr[i][j]  # Dữ liệu ban đầu cho arrVH
                arrTG[j][i] = arr[i][j]  # Tạo ma trận chuyển vị

        # Chuyển đồ thị thành vô hướng bằng cách bổ sung cạnh
        for i in range(n):
            for j in range(n):
                if arrVH[i][j] == 1:
                    arrVH[j][i] = 1

        # Kiểm tra liên thông của đồ thị
        visited = [0] * n
        arrIndex = []  # Danh sách đỉnh duyệt theo dfs
        indexStack = [0]
        count = 0  # Đếm số thành phần liên thông

        # Kiểm tra liên thông với đồ thị vô hướng
        for i in range(n):
            if visited[i] == 0:
                count += 1
                dfs1(visited, i, arrVH, n)

        # Kiểm tra điều kiện liên thông
        if count != 1:
            print("Not Connected At All")
        else:
            count = 0
            visited = [0] * n
            dfs(visited, 0, arr, n, arrIndex, indexStack)  # Duyệt từ đỉnh 0
            # Kiểm tra mức độ liên thông
            if len(arrIndex) != n:
                print("Weakly Connected")
            else:
                # Kiểm tra liên thông mạnh
                visited = [0] * n
                for i in arrIndex:
                    if visited[i] == 0:
                        count += 1
                        dfs1(visited, i, arrTG, n)
                if count == 1:
                    print("Strongly Connected")
                else:
                    print("Weakly Connected")

if __name__ == "__main__":
    main()