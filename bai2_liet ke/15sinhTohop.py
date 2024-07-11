def generate_combinations(n, k):
    # Tạo một mảng chứa các số từ 1 đến n
    numbers = [i for i in range(1, n + 1)]

    # Tạo một danh sách để lưu trữ tất cả các tổ hợp
    combinations = []

    # Hàm đệ quy để sinh ra tất cả các tổ hợp
    def backtrack(start, combination):
        # Nếu độ dài của tổ hợp bằng k, tức là chúng ta đã tạo ra một tổ hợp hoàn chỉnh
        if len(combination) == k:
            # Thêm tổ hợp vào danh sách
            combinations.append(combination[:])
            return

        # Duyệt qua tất cả các vị trí từ start đến n
        for i in range(start, n):
            # Thêm số tại vị trí i vào tổ hợp
            combination.append(numbers[i])
            # Tiếp tục sinh tổ hợp với vị trí bắt đầu là i + 1
            backtrack(i + 1, combination)
            # Xóa số cuối cùng để thử số tiếp theo
            combination.pop()

    # Bắt đầu quá trình sinh tổ hợp từ vị trí 0 và tổ hợp rỗng ban đầu
    backtrack(0, [])

    return combinations

if __name__ == "__main__":
    # Nhập hai số nguyên dương n và k
    n, k = map(int, input().split())

    # Tạo và in ra tất cả các tổ hợp chập k của n số tự nhiên từ 1 đến n
    combinations = generate_combinations(n, k)
    for combination in combinations:
        print(" ".join(map(str, combination)))