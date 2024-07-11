def dfs(n, m, y, x, garden):
   
    if y < 1 or y > n or x < 1 or x > m or garden[y - 1][x - 1] == 1:
        return 0 #ko hợp lệ trả về 0

    # Ô hiện tại nếu đã đi qua thì đánh là 1
    garden[y - 1][x - 1] = 1

    # Tìm kiếm các ô kề cận \: ....
    #trả về tổng số lượng ô có thể tiếp cận từ vị trí hiện tại
    """
    y-1: tìm kiếm ô ở trên
    y+1: tìm kiếm ô ở dưới
    x-1: tìm kiếm ô bên trái
    x+1: tìm kiếm ô bên phải
    """
    return 1 + \
        dfs(n, m, y - 1, x, garden) + \
        dfs(n, m, y + 1, x, garden) + \
        dfs(n, m, y, x - 1, garden) + \
        dfs(n, m, y, x + 1, garden)


if __name__ == "__main__":
    # Nhập kích thước vườn và vị trí bắt đầu
    n, m, y, x = map(int, input().split())

    # Khởi tạo ma trận biểu diễn vườn
    garden = []
    for i in range(n):
        row = list(map(int, input().split()))
        garden.append(row)

    # Thực hiện tìm kiếm chiều sâu và in kết quả
    an_rau = dfs(n, m, y, x, garden)
    print(an_rau)