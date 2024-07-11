#trả lại 1000$ cho khách bằng cách sử dụng ít tờ tiền nhất
# các mệnh giá cho sẵn: 1$, 5$, 10$, 50$, 100$, 500$
#-> giải quyết: chọn tờ tiền mệnh giá lớn nhất trước cho đến khi số tiền còn lại bằng 0

menh_gia = [500, 100, 50, 10, 5, 1]
money = 1000
n = int(input())

while (n): #duyệt từng testcase cho đến khi n bằng 0
    pay = int(input()) #nhập số tiền khách thanh toán
    mark = 0 #theo dõi vị trí hiện tại của tờ tiền trong danh sách mệnh giá
    count = 0 #đếm số lượng tờ tiền đã sử dụng
    remain = money - pay #tính tiền thừa cần trả lại
    while True:
        if remain == 0:
            print(count)
            break

        if remain < menh_gia[mark]:
            mark += 1
        else:
            remain -= menh_gia[mark]
            count += 1
    n -= 1