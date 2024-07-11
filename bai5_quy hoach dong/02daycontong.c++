#include <iostream>
#include <bits/stdc++.h>

using namespace std;

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

int sub(int x, int y, int k)
{
    int tmp = (x - y) % k;
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
    int **f = new int *[n + 1];
    for (int i = 0; i < n + 1; i++)
    {
        f[i] = new int[k];
    }
    // optimize
    f[0][0] = 0;
    for (int t = 1; t < k; t++)
        f[0][t] = INT_MAX;
    for (int i = 1; i <= n; i++)
    {
        for (int t = 1; t < k; t++)
        {
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