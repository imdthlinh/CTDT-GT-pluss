def dfs(visited, index, arr, n): #index chỉ số của đỉnh hiện tại, arr ma trận kề
    visited[index] = 1
    
    for i in range(n):  # Duyệt qua mỗi đỉnh trong đồ thị
        # Nếu có đường đi từ đỉnh index đến i và đỉnh i chưa được duyệt
        if arr[index][i] == 1 and index != i and visited[i] == 0:
            dfs(visited, i, arr, n)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]  # Nhập ma trận kề của đồ thị

        for i in range(n):
            visited = [0] * n 
            
            dfs(visited, i, arr, n)
            
            print("From%4d can visit: " % i, end='')
            
            first = True  # Biến kiểm tra xem có phải in đỉnh đầu tiên không
            for j in range(n):
                # Nếu đỉnh j đã được thăm và không phải đỉnh xuất phát
                if j != i and visited[j] == 1:
                    if not first:
                        print(',', end='')
                    else:
                        first = False
                    print("%3d" % j, end='')
            
            # Nếu không có đỉnh nào được thăm ngoại trừ chính nó
            if first:
                print("No vertex", end='')
            
            print() 
        print()

if __name__ == "__main__":
    main()