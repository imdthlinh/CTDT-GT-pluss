#include <iostream>
using namespace std;

const int MAX = 20; // Khai báo hằng số MAX là 20
const int N = 8; // Khai báo hằng số N là 8 (có thể hiểu là bàn cờ 8x8)

int x, y; // Khai báo hai biến nguyên x và y
bool a[MAX], b[MAX * 2], c[MAX * 2]; // Khai báo ba mảng bool a, b và c
int res[MAX]; // Khai báo mảng nguyên res

void print_solution()
{
    for (int i = 1; i <= N; i++)
    {
        cout << res[i] << " "; // In ra vị trí của từng hậu trong giải pháp
    }
    cout << endl;
}

bool is_safe(int row, int col)
{
    // Kiểm tra xem có đặt hậu vào vị trí (row, col) an toàn không
    return (!a[row] && !b[row + col - N] && !c[N - row + col]);
}

void Try(int col)
{
    if (col == N + 1)
    {
        print_solution(); // Nếu đã đặt hậu ở tất cả các cột, in ra giải pháp
    }
    else if (col == x)
    {
        Try(col + 1); // Nếu cột hiện tại là cột đã đặt hậu ban đầu, tiếp tục với cột tiếp theo
    }
    else
    {
        for (int row = 1; row <= N; row++)
        {
            if (is_safe(row, col))
            {
                // Đặt hậu vào vị trí (row, col)
                a[row] = 1;
                res[col] = row;
                b[row + col - N] = 1;
                c[N - row + col] = 1;

                Try(col + 1); // Tiếp tục thử đặt hậu ở cột tiếp theo

                // Xóa hậu khỏi vị trí (row, col)
                a[row] = 0;
                b[row + col - N] = 0;
                c[N - row + col] = 0;
            }
        }
    }
}

int main()
{
    cin >> x >> y; // Nhập vào vị trí ban đầu của một hậu
    // Đặt hậu vào vị trí (x, y) ban đầu
    a[y] = 1;
    res[x] = y;
    b[y + x - N] = 1;
    c[N - y + x] = 1;

    Try(1); // Bắt đầu thử đặt hậu từ cột 1

    return 0;
}

