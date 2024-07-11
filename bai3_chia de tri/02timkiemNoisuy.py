def tim_kiem(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right and x >= arr[left] and x <= arr[right]:
        if left == right:
            if arr[left] == x:
                return left
            else:
                return -1

        pos = left + int(((right - left) / (arr[right] - arr[left])) * (x - arr[left]))

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            left = pos + 1
        else:
            right = pos - 1

    return -1

def sap_xep(arr):
    return sorted(arr)

d = int(input())
arr = [int(x) for x in input().split()]
n = int(input())
queries = [int(input()) for _ in range(n)]

arr = sap_xep(arr)
print(" ".join(map(str, arr)))

for x in queries:
    pos = tim_kiem(arr, x)
    print(pos)