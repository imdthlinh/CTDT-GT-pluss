def sinh_day_NhiPhan(n):
    day_NhiPhan = [] #danh sach luu tru cac day nhi phan
    dayNhiPhan_dau = [0] * n #day nhi phan dau tien voi n so 0

    while True: #vong lap vo han sinh cac day nhi phan
        print(''.join(str(x) for x in dayNhiPhan_dau))
        #tim so 0 cuoi cung
        i = n-1
        while i >= 0 and dayNhiPhan_dau[i] == 1:
            i -= 1
        #kiem tra dieu kien dung:
        if i < 0:
            break #thoat khoi vong lap khi da sinh het day nhi phan
        #Doi so 0 thanh 1:
        dayNhiPhan_dau[i] = 1
        #Doi cac so 1 phia sau thanh 0:
        for j in range(i + 1, n):
            dayNhiPhan_dau[j] = 0
n = int(input())
sinh_day_NhiPhan(n)
