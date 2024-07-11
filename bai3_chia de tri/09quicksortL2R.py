def print_array(arr, l, r):
    for i in range(l, r + 1):
        print(arr[i], end=" ")
    print()

def swap(a, b): #Hàm hoán đổi a và b và trả về hai giá trị đã hoán đổi
    t = a
    a = b
    b = t
    return a, b

def partition(arr, l, r):
    pivot = arr[r]  #sử dụng phần tử cuối cùng (arr[r]) làm pivot để phân đoạn mảng
    i = l #Dùng hai biến i và j để duyệt từ đầu và cuối mảng về phía nhau
    j = r - 1
    print(f"\nPartitioning: left={l}, right={r}")
    print_array(arr, l, r)

    while True:
        while i <= j and arr[i] > pivot:
            i += 1  # Điều chỉnh điều kiện để sắp xếp theo thứ tự giảm dần
        while i <= j and arr[j] <= pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = swap(arr[i], arr[j])
        print_array(arr, l, r)

    arr[i], arr[r] = swap(arr[i], arr[r])  # Hoán đổi pivot về vị trí cuối cùng
    print_array(arr, l, r)  # In mảng sau lần hoán đổi cuối
    return i

def quick_sort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quick_sort(arr, l, p - 1)
        quick_sort(arr, p + 1, r)

n = int(input())
arr = list(map(int, input().split()))
print_array(arr, 0, n - 1)  # In mảng ban đầu
quick_sort(arr, 0, n - 1)
print_array(arr, 0, n - 1)  # In mảng đã sắp xếp