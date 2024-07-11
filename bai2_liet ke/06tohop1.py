def try_func(i, j): #hàm này để tìm và in ra các dãy số
    global n, k, a #khai báo biến toàn cục
    for t in range(j, n+1): #sd vòng lặp để duyệt qua các số từ j đến n
        a[i] = t #gán gtri t vào ptu thứ i của ds a -> build dãy số
        if i == k - 1: #nếu đã đến ptu cuối thì in ra dãy số đó
            #in kết quả dùng hàm join để nối các ptu của ds a thành một chuỗi, cách nhau = dấu cách
            print(" ".join(str(x) for x in a))
        else: #nếu chưa đến ptu cuối thì gọi đệ quy hàm try với i+1,t+1 để tiếp tục build dãy số
            try_func(i + 1, t + 1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [0] * k #khởi tạo ds a với k ptu = 0, ctdl để lưu trữ dãy số đang build
    try_func(0, 1) #gọi hàm try với i=0 và j=1 để bắt đầu tìm kiếm và build dãy số