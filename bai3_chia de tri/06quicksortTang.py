def quick_sort(arr, low, high):
    if low < high:
        # Tìm phần tử chia nhóm (pivot)
        pi = partition(arr, low, high)
        # Đệ quy sắp xếp các nhóm con trước và sau pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Chọn phần tử cuối cùng làm pivot
    i = low - 1  # Chỉ số của phần tử nhỏ hơn pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            # Tăng chỉ số của phần tử nhỏ hơn pivot và đổi chỗ nó với phần tử tại chỉ số i
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Đổi chỗ pivot với phần tử tại chỉ số i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Nhập dữ liệu
n = int(input())
arr = list(map(int, input().split()))

# Sắp xếp mảng
quick_sort(arr, 0, n - 1)

# In ra mảng đã sắp xếp
print(*arr)