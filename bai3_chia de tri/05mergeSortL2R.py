def print_array(arr, l, r): #Hàm in các phần tử của mảng arr từ chỉ số l đến r
    for i in range(l, r+1):
        print(arr[i], end=" ")

def merge(arr, l, m, r): #Hàm gộp hai mảng con đã sắp xếp
    n1 = m - l + 1 #Số ptu trong mảng con trái
    n2 = r - m #Số ptu trong mảng con phải

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):  #Sao chép các phần tử từ mảng arr vào hai mảng L và R
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2: #so sánh từng phần tử từ L và R và đặt phần tử nhỏ hơn vào vị trí hiện tại của arr
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1: #Sao chép các phần tử còn lại của L và R vào arr nếu có
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    print(f"\nMerge: {l} --> {m} and {m+1} --> {r}")
    print_array(arr, l, r)
    print()

def merge_sort(arr, l, r): #Định nghĩa hàm merge_sort để sắp xếp mảng bằng thuật toán merge sort
    if l < r:
        m = l + (r - l) // 2 #Tính chỉ số giữa m

        print(f"\nDivide: {l} --> {m} and {m+1} --> {r}")
        print_array(arr, l, m)
        print(":: ", end="")
        print_array(arr, m+1, r)

        merge_sort(arr, l, m) #Đệ quy gọi merge_sort để sắp xếp mảng con trái và phải
        merge_sort(arr, m + 1, r)

        merge(arr, l, m, r) #Gộp hai mảng con đã sắp xếp lại với nhau bằng hàm merge

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(" ", end="")
    print_array(arr, 0, n - 1)

    merge_sort(arr, 0, n - 1) #Gọi hàm merge_sort để sắp xếp mảng arr từ chỉ số 0 đến n-1