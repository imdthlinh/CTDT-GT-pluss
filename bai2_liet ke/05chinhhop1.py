def quay_lui(vi_tri): #vị trí hiện tại trong dãy số đang được xây dựng
    if vi_tri == k: #ktra vị trí hiện tại có bằng độ dài mục tiêu k ko
        #nếu bằng thì tìm được dãy số hợp lệ, in ra dãy số đó và trả về khỏi hàm
        print(*a)
        return

    for i in range(1, n+1): #bắt đầu một vòng lặp duyệt qua các số từ 1-n, 
        #đây là thuật toán quay lui, thử từng số có sẵn tại vị trí hiện tại
        if not da_chon[i-1]:#ktra xem liệu số hiện tại i đã sử dụng chưa
            da_chon[i-1] = 1 #sử dụng da_chon[i-1] vì các số trong ds da_chon bắt đầu từ 0, trong khi các số xét bắt đầu từ 1
            #nếu số hiện tại i chưa đc sdung, đánh dấu nó là đã đc sdung bằng cách đặt = 1
            a[vi_tri] = i #gán số hiện tại i vào vtri trong ds a
            quay_lui(vi_tri + 1) #đệ quy hàm quay_lui với vtri tiếp theo để xây dựng dãy số
            da_chon[i-1] = 0 #sau khi đệ quy, đặt lại da_chon = 0 để dánh dấu số hiện tại là có sẵn cho lần lặp tiếp

n, k = map(int, input().split()) #map để chuyển đổi chuỗi đầu vào thành số nguyên
a = [0] * k #tạo ds a có độ dài k, tất cả các phần tử được khởi tạo = 0, ds này lưu trữ dãy số cuối cùng
da_chon = [0] * n #tạo ds đã da_chon độ dài n, các ptử đc khởi tạo = 0, ds theo dõi các số đc sử dụng trong dãy số 
quay_lui(0) #gọi hàm quay_lui với vtri ban đầu là 0 để bắt đầu quá trình quay lui