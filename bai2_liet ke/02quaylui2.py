def lietke_dayNhiPhan(n):
    def day_nhiphan(day_hientai, index):
        if index == n:
            result.append(day_hientai)
            return
        
        day_nhiphan(day_hientai + "0", index + 1)

        day_nhiphan(day_hientai + "1", index + 1)
    result = []
    day_nhiphan("", 0)
    result.sort(reverse=True)
    for day_so in result:
        print(day_so)
n = int(input())
lietke_dayNhiPhan(n)