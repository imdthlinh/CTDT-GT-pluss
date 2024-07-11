def quay_lui(nums, hoan_vi, result):
    if len(hoan_vi) == len(nums):
        result.append(hoan_vi[:])
        return

    for i in range(len(nums)):
        if nums[i] not in hoan_vi:
            hoan_vi.append(nums[i])
            quay_lui(nums, hoan_vi, result)
            hoan_vi.pop()

def hoan_doi(nums):
    result = []
    quay_lui(nums, [], result)
    result.sort()
    return result

# Nhập số lượng n và n số tự nhiên khác nhau
n = int(input())
nums = [int(x) for x in input().split()]

# Liệt kê tất cả hoán vị và in ra
for perm in hoan_doi(nums):
    print(' '.join(map(str, perm)))