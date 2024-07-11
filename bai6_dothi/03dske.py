def set(a, n):
    for i in range(n):
        a[i] = 0

def main():
    t = int(input())
    for k in range(t):
        n = int(input()) #số đỉnh của đồ thị
        #Tạo một ma trận n x n và khởi tạo tất cả các phần tử bằng 0 (ma trận kề)
        a = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            row = list(map(int, input().split()))
            for j in range(n):
                a[i][j] = row[j]
        
        #chạy qua từng đỉnh i của đồ thị
        for i in range(n):
            #danh sách a1 gồm 100 phần tử và đặt tất cả các phần tử của a1 bằng 0
            a1 = [0] * 100
            m = 0 #biến đếm số đỉnh kề của đỉnh i
            set(a1, 100)
            print(f"Vertex{i:4d}:", end="")
            #chạy qua các cột j của ma trận kề
            for j in range(n):
                if a[i][j] == 1:
                    a1[m] = j
                    m += 1
            #chạy qua các phần tử trong danh sách a1 đến m
            for h in range(m):
                if h == m - 1:
                    print(f" {a1[h]}", end="\n")
                else:
                    print(f" {a1[h]},", end="")
        print()

if __name__ == "__main__":
    main()