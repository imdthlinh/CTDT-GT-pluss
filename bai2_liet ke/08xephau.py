def check(r, c): #hàm kiểm tra vị trí có bị hậu khác ăn không
    for i in range(c):
        if board[i] == r or abs(i - c) == abs(board[i] - r):
            return False
    return True

def printSolution(): #hàm in vị trí hợp lệ
    global dem
    dem += 1
    print(f"Solution {dem}: ", end="")
    for i in range(n):
        print(board[i] + 1, end=" ")
    print()

def backtrack(c): #thử đặt quân hậu theo đệ quy
    for r in range(n):
        if check(r, c):
            board[c] = r
            if c == n - 1:
                printSolution()
            else:
                backtrack(c + 1)

if __name__ == "__main__":
    n = int(input())
    board = [0] * n
    dem = 0

    backtrack(0)