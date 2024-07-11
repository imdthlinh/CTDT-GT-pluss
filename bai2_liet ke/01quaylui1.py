def lietke_dayNhiPhan(n):
    def day_nhiphan(day_hientai, index):
        if index == n:
            print(day_hientai)
            return
        
        day_nhiphan(day_hientai + "0", index + 1)

        day_nhiphan(day_hientai + "1", index + 1)
    day_nhiphan("", 0)
n = int(input())
lietke_dayNhiPhan(n)