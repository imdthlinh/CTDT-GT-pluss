import numpy as np

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        #Tạo một ma trận n x n gồm các số nguyên và khởi tạo tất cả các phần tử bằng 0
        a = np.zeros((n, n), dtype=int)
        #chạy n lần để đọc n dòng tiếp theo từ đầu vào và gán vào các hàng tương ứng của ma trận a
        for i in range(n):
            a[i] = [int(x) for x in input().split()]
        
        a1 = []
        b1 = []
        for i in range(n):
            for j in range(n):
                if a[i][j] != 0:
                    a1.append(i)
                    b1.append(j)
        
        print(", ".join(f"({a1[i]}, {b1[i]})" for i in range(len(a1))))

if __name__ == "__main__":
    main()

