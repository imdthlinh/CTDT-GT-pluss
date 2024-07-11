def generate_permutations(n):
    # Khởi tạo một mảng chứa các số từ 1 đến n
    numbers = [i for i in range(1, n + 1)]

    # Tạo một danh sách để lưu trữ tất cả các hoán vị
    permutations = []

    # Hàm đệ quy để sinh ra tất cả các hoán vị
    def backtrack(start):
        # Nếu chỉ số bắt đầu bằng n - 1, tức là chúng ta đã tạo ra một hoán vị hoàn chỉnh
        if start == n - 1:
            # Thêm hoán vị vào danh sách
            permutations.append(numbers[:])

        # Duyệt qua tất cả các vị trí từ start đến n
        for i in range(start, n):
            # Hoán đổi số tại vị trí start và i
            numbers[start], numbers[i] = numbers[i], numbers[start]
            # Tiếp tục sinh hoán vị với vị trí bắt đầu là start + 1
            backtrack(start + 1)
            # Đảo ngược lại hoán vị để tiếp tục sinh các hoán vị khác
            numbers[start], numbers[i] = numbers[i], numbers[start]

    # Bắt đầu quá trình sinh hoán vị từ vị trí 0
    backtrack(0)

    # Sắp xếp các hoán vị theo thứ tự giảm dần
    permutations.sort(reverse=True)

    return permutations

if __name__ == "__main__":
    # Nhập số nguyên dương n
    n = int(input())

    # Tạo và in ra tất cả các hoán vị của n số tự nhiên từ 1 đến n
    permutations = generate_permutations(n)
    for permutation in permutations:
        print(" ".join(map(str, permutation)))