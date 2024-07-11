#include <iostream>
#include <cstring>

using namespace std;

// Hàm để in bảng F
void in(int **f, int m, int n)
{
    cout << "   F";
    for (int i = 0; i <= n; i++)
    {
        printf("%4d", i); // In tiêu đề cột
    }
    cout << endl;
    for (int i = 0; i <= m; i++)
    {
        printf("%4d", i); // In tiêu đề hàng
        for (int j = 0; j <= n; j++)
        {
            printf("%4d", f[i][j]); // In giá trị của bảng F
        }
        cout << endl;
    }
}

// Hàm để tìm giá trị nhỏ nhất của ba số
int min3(int x, int y, int z)
{
    int tmp = x < y ? x : y;
    return z < tmp ? z : tmp;
}

int main()
{
    int m, n;
    cin >> m >> n; // Đọc độ dài của hai chuỗi

    // Khởi tạo bảng F
    int **f = new int *[m + 1];
    for (int i = 0; i < m + 1; i++)
    {
        f[i] = new int[n + 1];
    }

    string X, Y;
    cin >> X >> Y; // Đọc hai chuỗi X và Y

    // Khởi tạo hàng đầu tiên và cột đầu tiên của bảng F
    for (int i = 0; i <= m; i++)
        f[i][0] = i;

    for (int j = 0; j <= n; j++)
        f[0][j] = j;

    // Tính toán khoảng cách chỉnh sửa
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (X[i - 1] == Y[j - 1])
            {
                f[i][j] = f[i - 1][j - 1]; // Ký tự giống nhau, không cần chỉnh sửa
            }
            else
            {
                // Tính toán giá trị nhỏ nhất của ba phép chỉnh sửa: chèn, thay thế, hoặc xóa
                f[i][j] = min3(f[i][j - 1], f[i - 1][j - 1], f[i - 1][j]) + 1;
            }
        }
    }

    in(f, m, n); // Gọi hàm in để in bảng F

    // Tính toán chuỗi chỉnh sửa
    int count = 0; // Đếm số lượng các phép chỉnh sửa

    while (m >= -1 && n >= -1)
    {
        if (X[m - 1] == Y[n - 1])
        {
            m--; // Ký tự giống nhau, chuyển đến cặp ký tự tiếp theo
            n--;
        }
        else
        {
            if (f[m][n] == f[m][n - 1] + 1) // Phép chèn
            {
                if (n > 0)
                {
                    count++;
                }
                n--; // Chuyển đến ký tự tiếp theo trong Y
            }
            else if (f[m][n] == f[m - 1][n - 1] + 1) // Phép thay thế
            {
                if (n > 0 && m > 0) // Cả hai chuỗi đều chưa đến đầu
                {
                    count++;
                }
                m--; // Chuyển đến ký tự trước đó trong X
                n--;
            }
            else // Phép xóa
            {
                if (m > 0)  // Ký tự cần xóa không phải là ký tự đầu tiên
                {
                    count++;
                }
                m--;
            }
        }
    }

    cout << count << endl; // In ra số lượng các phép chỉnh sửa
    // Backtracking để tìm chuỗi chỉnh sửa
    m = X.length(), n = Y.length();

    while (m >= -1 && n >= -1)
    {
        // Nếu ký tự hiện tại của X và Y giống nhau, chuyển đến ký tự trước đó
        if (X[m - 1] == Y[n - 1])
        {
            m--;
            n--;
        }
        else
        {
            // Nếu ký tự hiện tại của X và Y không giống nhau, có ba phép chỉnh sửa có thể thực hiện:
            if (f[m][n] == f[m][n - 1] + 1) // Phép chèn
            {
                if (n > 0)
                {
                    printf("Insert(%d,%c)\n", m, Y[n - 1]);
                }
                n--;
            }
            else if (f[m][n] == f[m - 1][n - 1] + 1) // Phép thay thế
            {
                if (n > 0 && m > 0)
                {
                    printf("Replace(%d,%c)\n", m, Y[n - 1]);
                }
                m--;
                n--;
            }
            else // Phép xóa
            {
                if (m > 0)
                {
                    printf("Delete(%d)\n", m);
                }
                m--;
            }
        }
    }

    return 0;
}