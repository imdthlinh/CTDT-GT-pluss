def max_count(n_arr, n, count):
    if n == 0:
        return (-1, count)

    if n == 1:
        return (int(n_arr[0]), count)

    n_max, d_count = max_count(n_arr, n - 1, count)
    
    if int(n_arr[n - 1]) > int(n_max):
        d_count = 1

        return (int(n_arr[n - 1]), d_count)
    elif int(n_arr[n - 1]) == int(n_max):
        d_count += 1
        return (int(n_arr[n - 1]), d_count)
        
    else:
    
        return (int(n_max), d_count)
    

if __name__ == "__main__":
    t = int(input())

    arr = []

    for i in range(0,t):
        a = input()
        arr.append(a)

    for n in arr:
        _, a = max_count(n, len(n), 1)
        print("{}: {}".format(n, a))
