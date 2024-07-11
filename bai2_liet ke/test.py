def is_safe(board, row, col):
    # Kiểm tra xem có quân hậu nào ăn được quân hậu tại vị trí (row, col) không
    # Kiểm tra hàng ngang
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Kiểm tra đường chéo trên
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Kiểm tra đường chéo dưới
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_eight_queens(board, col):
    # Nếu tất cả 8 quân hậu đã được đặt, trả về True
    if col == 8:
        print(' '.join(map(str, [j+1 for j in range(8) if board[j][i] == 1])))
        return True
  
    # Đặt quân hậu tại từng hàng trong cột hiện tại
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            
            # Đệ quy để đặt các quân hậu còn lại
            if solve_eight_queens(board, col + 1):
                return True

            # Nếu đặt quân hậu tại vị trí (i, col) không dẫn đến giải pháp,移除
            board[i][col] = 0

    # Nếu không thể đặt quân hậu trong cột này, trả về False
    return False

# Đọc vị trí của quân hậu đầu tiên từ người dùng
y, x = map(int, input().split())

# Tạo bảng cờ ban đầu
board = [[0 for _ in range(8)] for _ in range(8)]
board[y-1][x-1] = 1

# Giải quyết bài toán
solve_eight_queens(board, 0)