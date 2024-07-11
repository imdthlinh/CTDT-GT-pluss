#include <iostream>
#include <bits/stdc++.h>

using namespace std;

//f là một mảng động 2 chiều được sử dụng để lưu trữ thông tin về các dãy con có tổng chia hết cho k.
//Mỗi phần tử f[i][t] lưu trữ độ dài của dãy con tối thiểu có tổng chia dư t khi chọn các phần tử từ A[0] đến A[i-1].

void in(int **f, int n, int k)
{
    cout << " n/t";
    for (int i = 0; i < k; i++)
    {
        printf("%4d", i);
    }
    cout << endl;
    for (int i = 0; i <= n; i++)
    {
        printf("%4d", i);
        for (int t = 0; t < k; t++)
        {
            if (f[i][t] == INT_MAX)
            {
                cout << " +00";
            }
            else
            {
                printf("%4d", f[i][t]);
            }
        }
        cout << endl;
    }
}
//tính phần dư khi chia tổng các phần tử của mảng A cho k.
int sub(int x, int y, int k)
{
    int tmp = (x - y) % k;       //lay phan du
    return tmp >= 0 ? tmp : tmp + k;
}

int main()
{
    int n, k, sum = 0;
    cin >> n >> k;
    int A[n];
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
        sum += A[i];
    }
    if (sum % k == 0)
    {
        cout << "Day da cho thoa man yeu cau." << endl
             << "Tong =" << sum;
        return 0;
    }
    int **f = new int *[n + 1];     //khai bao con tro 2 chieu cap phat dong cho 1 mang n + 1 phan tu
    for (int i = 0; i < n + 1; i++)
    {
        f[i] = new int[k];        //Với mỗi phần tử i của mảng f, ta cấp phát động một mảng int có k phần tử.
    }
    // toi uu
    f[0][0] = 0;            //dat phan tu dau tien bang 0
    for (int t = 1; t < k; t++)
        f[0][t] = INT_MAX;           //gia tri con lai của hàng dau tien cua mang f 
    for (int i = 1; i <= n; i++)
    {
        for (int t = 1; t < k; t++)
        {  //Với mỗi phần tử A[i-1] trong mảng A, thuật toán sẽ kiểm tra xem nếu thêm A[i-1] vào dãy con hiện tại (f[i-1][t]) thì tổng có chia hết cho k không.
           //Nếu tổng chia hết cho k, thuật toán sẽ giữ nguyên dãy con hiện tại (f[i-1][t]).
           //Nếu tổng không chia hết cho k, thuật toán sẽ thêm A[i-1] vào dãy con hiện tại và tăng độ dài dãy con lên 1 (f[i-1][sub(t, A[i-1], k)] + 1)
            if (f[i - 1][t] < f[i - 1][sub(t, A[i - 1], k)] + 1)   
                f[i][t] = f[i - 1][t];
            else
                f[i][t] = f[i - 1][sub(t, A[i - 1], k)] + 1;
        }
    }
    in(f, n, k);
    cout << "Chieu dai day con: " << n - f[n][sum % k] << endl;
    // truy vet
    int t = sum % k;
    sum = 0;
    for (int i = n; i >= 1; i--)
    {
        if (f[i][t] == f[i - 1][t])
        {
            printf("a[%d]=%d;", i, A[i - 1]);
            sum += A[i - 1];
        }
        else
        {
            t = sub(t, A[i - 1], k);
        }
    }
    cout << endl
         << "Tong =" << sum;
    return 0;
}