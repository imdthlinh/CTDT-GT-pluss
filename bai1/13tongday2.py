def tong_day(n):
    if n == 1:
        return 1.0 / 2
    return tong_day(n - 1) + n / (n + 1)

def main():
    t = int(input()) 
    while t > 0:
        n = int(input())  
        result = tong_day(n)  
        print(f"{result:.10f}") 
        t -= 1

if __name__ == "__main__":
    main()
