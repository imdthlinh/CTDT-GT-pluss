def try_func(i, j):
    global n, k, a
    for t in range(n, j-1, -1): #vòng lặp duyệt các số từ n->j theo thứ tự giảm dần
    #khi a[i] được gán gtri, 
        a[i] = t
        #nếu i đã đạt đến k-1, tức là đã hoàn thành 1 tổ hợp
        if i == k - 1:
            #sử dụng sorted để sắp xếp các ptu trong a theo thứ tự giảm dần và in ra dãy số đó
            print(" ".join(str(x) for x in sorted(a, reverse=True)))
        else: #nếu i chưa đạt đến k-1 thì gọi đệ quy try để tiếp tục tìm kiếm tổ hợp khác
            try_func(i + 1, t + 1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [0] * k
    try_func(0, 1)