import sys

def tsp_greedy(distances):
    # lấy số thành phố
    n = len(distances)
    
    # khởi tạo danh sách các thành phố và đánh dấu thành phố đầu tiên là đã đi qua
    visited = [False] * n
    visited[0] = True
    
    # đặt thành phố hiện tại là thành phố đầu tiên và tổng khoảng cách = 0
    curr_city = 0
    total_distance = 0
    path = ["1"]

    # Lặp qua các thành phố còn lại và tìm thành phố có khoảng cách ngắn nhất với thành phố hiện tại
    for i in range(n-1):
        next_city = -1
        min_distance = sys.maxsize

        for j in range(n):
            # Nếu thành phố không đc ghé thăm và khoảng cách nhỏ hơn min_distance
            if not visited[j] and distances[curr_city][j] < min_distance:
                next_city = j
                min_distance = distances[curr_city][j]

        # Đánh dáu TP đã chọn là đã ghé thăm, cập nhật TP hiện tại và thêm k/c vào tổng quãng đường đã đi
        visited[next_city] = True
        curr_city = next_city
        total_distance += min_distance

        path.append("{}({})".format(curr_city + 1, min_distance))

    # Cộng k/c về TP đầu tiên để hoàn thành vòng lặp và trả về tổng quãng đường đã đi
    path.append("1({})".format(distances[curr_city][0]))
    total_distance += distances[curr_city][0]

    return total_distance, path

# Đọc ma trận đầu vào của k/c
n = int(input())

distances = []

for i in range(n):
    row = list(map(int, input().split()))
    distances.append(row)

# Giải TSP bằng thuật toán tham lam bắt đầu từ TP đầu tiên
min_distance, tsp_path = tsp_greedy(distances)

# In quãng đường tối thiểu mà nhân viên bán hàng đã đi
print("Tong chi phi={}".format(min_distance))
print("->".join(tsp_path))