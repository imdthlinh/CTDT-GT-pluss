def binary_search(arr, target):
    """
        arr (list): Mảng đã sắp xếp.
        target (int): Giá trị cần tìm.

        KQ:
        int: Chỉ số của target trong mảng arr nếu nó tồn tại, -1 nếu không tồn tại.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

if __name__ == "__main__":
    # Đọc dữ liệu đầu vào
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    # Sắp xếp mảng theo thứ tự giảm dần
    arr.sort(reverse=True)

    # In mảng đã sắp xếp
    print(" ".join(map(str, arr)))

    # Tìm kiếm và in vị trí của các số trong mảng đã sắp xếp
    for _ in range(m):
        x = int(input())
        index = binary_search(arr, x)
        print(index)