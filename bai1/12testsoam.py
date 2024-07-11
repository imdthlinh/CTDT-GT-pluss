def test_negative(arr):
    if len(arr) == 0:
        return True
    if arr[0] >= 0:
        return False
    return test_negative(arr[1:])


t = int(input())  # Số lượng testcase
results = []  # Danh sách lưu trữ kết quả

for _ in range(t):
    n = int(input())  # Số lượng phần tử của mảng
    arr = list(map(float, input().split()))  # Đọc dãy n số thực
    if test_negative(arr):
        results.append("Yes")
    else:
        results.append("No")

for result in results:
    print(result)