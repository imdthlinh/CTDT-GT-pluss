# - yêu cầu rút W tiền, atm phân phát N tiền sao cho tổng bằng W
# - cần thuật toán giảm thiểu số N tờ tiền cho mỗi giao dịch
# - các mệnh giá là: 1000, 2000, 3000, 5000, ^c
# - nguồn cấp tiền vô hạn
# -> giải quyết: 
# b1/bắt đầu từ mệnh giá lớn nhất 
# b2/nếu số tiền còn lại ko thể đc đổi bằng tờ mệnh giá lớn nhất thì 
# sử dụng tờ mệnh giá tiếp. 
# b3/lặp lại b2 cho đến khi đạt đến tổng W

import math

def atm_algorithm(w,c):

    # initialize variables
    menh_gia = [1000, 2000, 3000, 5000]

    # với mỗi test case
    for i in range(num_testcases):
        # kiểm tra có chia hết cho 1000 hay không, 
        # nếu không, thì dừng testcase và in ra 0 luôn
        if w[i] % 1000 != 0:
            print("0")
            continue
        
        count = 0 #số lượng tờ tiền đã sử dụng cho mỗi mệnh giá
        money = w[i] #sao chép số tiền cần rút vào money
        l = 1 #lưu trữ số cách phân phát tối thiểu
        
        # lặp từ dưới lên tìm mệnh giá to nhất
        for j in range(c[i], -1, -1): #duyệt các gtri c từ c[i] đến 0 theo thứ tự giảm dần
            arrtmp = [0, 0, 0, 0] #mảng để xét các trường hợp đặc biệt có nhiều hơn 1 cách chia
            
            # loop through each possible bill value
            for k in range(len(menh_gia) - 1, -1, -1): #duyệt các mệnh giá theo thứ tự giảm dần
                # Example 5000 x 10^c
                tmp = menh_gia[k] * 10**j #tính mệnh giá tiền dựa trên mệnh giá cơ bản và gtri c

                paper_needed = money // tmp #tính số lượng tờ tiền cần sử dụng cho mệnh giá hiện tại

                count += paper_needed #cộng số lượng tờ tiền đã tính đc
                
                # Trong trường hợp số tiền không chia hết thì thêm 1 tờ
                if paper_needed != 0:
                    arrtmp[k] = 1

                # update số tiền mới sau khi chia
                money %= tmp
            
            # cập nhật l dựa trên số tiền sự dụng tại hàng 10^j
            if arrtmp[3] == 1 and arrtmp[2] == 1 and arrtmp[0] == 1: #sử dụng 3 mệnh giá, có 3 cách phân phát
                l *= 3
            elif arrtmp[3] == 1 and arrtmp[0] == 1: #sử dụng 2 mệnh giá, có 2 cách phân phát
                l *= 2
            elif arrtmp[3] == 0 and arrtmp[2] == 1 and arrtmp[0] == 1: #sử dụng 1 mệnh giá, có 2 cách phân phát
                l *= 2
        
        #in ra tổng số tờ tiền đã sử dụng và số cách phân phát tối thiểu
        print(count, l)

#đọc dữ liệu input
num_testcases = int(input()) #nhập số lượng bộ dữ liệu

w = [] #danh sách w lưu trữ các số tiền cần rút
c = [] #danh sách c lưu trữ các giá trị c

#lặp lại các testcase
for i in range(num_testcases):
    # đọc các tham số đầu vào cho testcase hiện tại
    w_i = int(input()) # nhập số tiền cần rút
    c_i = int(input()) # nhập giá trị c vào cho bộ dữ liệu hiện tại

    w.append(w_i) # nhập số tiền cần rút vào danh sách w
    c.append(c_i) # nhập giá trị c vào danh sách c

atm_algorithm(w, c)