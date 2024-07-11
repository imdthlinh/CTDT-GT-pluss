def merge_sort(arr):
    if len(arr) <= 1: #nếu dãy có 1 ptu trở xuống thì in ra
        return arr

    mid = len(arr) // 2 #Tìm chỉ số phần tử giữa của mảng
    #Chia mảng thành hai phần: bên trái và bên phải
    left = arr[:mid]
    right = arr[mid:]
    
    #Đệ quy gọi hàm merge_sort trên từng phần
    left = merge_sort(left) 
    right = merge_sort(right)
    
    #Gộp hai phần đã sắp xếp thành một mảng mới và trả về
    return merge(left, right)

def merge(left, right): #kết hợp 2 mảng con thành 1 mảng mới
    result = []
    l_idx, r_idx = 0, 0

    #Lặp qua cả hai mảng con để so sánh và gộp
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

    result.extend(left[l_idx:])
    result.extend(right[r_idx:])

    return result

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = merge_sort(arr)
    print(" ".join(map(str, sorted_arr)))