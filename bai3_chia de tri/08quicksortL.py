def print_array(arr, l, r):
    for i in range(l, r + 1):
        print(arr[i], end=" ")
    print()

def partition(arr, l, r): #Hàm phân đoạn mảng arr từ chỉ số l đến r xung quanh giá trị pivot
    pivot = arr[l] #Ban đầu, pivot được chọn là phần tử đầu tiên của đoạn arr[l]
    i = l + 1 #i và j lần lượt là các chỉ số để duyệt qua mảng từ trái sang phải và từ phải sang trái
    j = r
    print(f"\nPartitioning: left={l}, right={r}")
    print_array(arr, l, r)
    
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1 #tăng i khi phần tử tại arr[i] nhỏ hơn hoặc bằng pivot
        while i <= j and arr[j] > pivot:
            j -= 1 #giảm j khi phần tử tại arr[j] lớn hơn pivot
        if i < j:
            arr[i], arr[j] = arr[j], arr[i] #hoán đổi arr[i] và arr[j]
            print_array(arr, l, r) #in mảng sau khi hoán đổi
            i += 1 #sau đó tăng i và giảm j
            j -= 1
    arr[l], arr[j] = arr[j], arr[l] #Sau khi phân đoạn xong, hoán đổi phần tử pivot với arr[j]
    print_array(arr, l, r) #in mảng sau khi hoán đổi cuối cùng
    return j #Trả về vị trí j của pivot

def quick_sort(arr, l, r): #Hàm xếp mảng arr từ chỉ số l đến r bằng thuật toán Quick Sort
    if l < r:
        p = partition(arr, l, r) #Gọi hàm partition để phân đoạn mảng và nhận lại vị trí p của pivot
        quick_sort(arr, l, p - 1) #Gọi đệ quy quick_sort cho đoạn mảng bên trái l đến p-1
        quick_sort(arr, p + 1, r) #đoạn mảng bên phải p+1 đến r

n = int(input())
arr = list(map(int, input().split()))
print_array(arr, 0, n - 1) #in mảng ban đầu
quick_sort(arr, 0, n - 1) 
print_array(arr, 0, n - 1) #in mảng sau khi sắp xếp