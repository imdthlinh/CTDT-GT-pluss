def sinh_to_hop(a, k, n):
  i = k - 1
  while i >= 0 and a[i] == n - k + i + 1:
    i -= 1
  if i < 0:
    return False
  a[i] += 1
  for j in range(i + 1, k):
    a[j] = a[i] + j - i
  return True

def in_to_hop(a, k):
  for i in range(k):
    print(a[i], end=" ")
  print()

n, k = map(int, input("Nhập n, k: ").split())

# Khởi tạo tổ hợp đầu tiên
a = [i + 1 for i in range(k)]

# Sinh và in ra các tổ hợp
while True:
  in_to_hop(a, k)
  if not sinh_to_hop(a, k, n):
    break