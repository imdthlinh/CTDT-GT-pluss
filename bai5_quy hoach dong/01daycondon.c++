#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// Hàm chuyển đổi chuỗi thành các số nguyên và lưu vào mảng A
void simple_tokenizer(string s, int A[])
{
    stringstream ss(s); 
    int i = 1;  
    string word;
    while (ss >> word) { 
        A[i++] = stoi(word);  
    }
}

int main()
{
    int n, jmax;
    cin >> n;  
    int A[n + 2], L[n + 2], T[n + 2];  
    // L: độ dài của dãy co tăng dài nhất kt tại mỗi phần tử
    //T được dùng để lưu vị trí của phần tử tiếp theo trong dãy con tăng dài nhất
    string s;
    getline(cin, s);  // Đọc bỏ dòng đầu tiên (dòng trống)
    getline(cin, s);  // Đọc chuỗi chứa các số nguyên

    if(s.empty()) {  
        // Sử dụng mảng mặc định nếu chuỗi đầu vào rỗng
        int tmp[] = {1, 2, 3, 4, 9, 10, 5, 6, 7};
        int index = 0;
        for(int i = 1; i <= n; i++) {
            A[i] = tmp[index++];  // Gán giá trị từ mảng tmp vào mảng A
        }
    } else {
        simple_tokenizer(s, A);  // Chuyển đổi chuỗi thành mảng số nguyên
    }

    // Khởi tạo mảng
    L[n] = 0;  // Đặt giá trị ban đầu của L[n] là 0
    L[n + 1] = 1;  // Đặt giá trị của L[n+1] là 1
    printf("L[%d]=1\n", n + 1);  // In ra giá trị khởi tạo của L[n+1]

    // Tính toán giá trị của L và T
    for(int i = n; i >= 0; i--) { 
        jmax = n + 1;  
        printf("jmax=n+1=%d+1=%d\n", n, n + 1);  
        for(int j = i + 1; j <= n + 1; j++) {  
            if( ((i == 0 || j == n + 1) || A[j] > A[i]) && L[j] > L[jmax]) {
                // Kiểm tra điều kiện nếu A[j] lớn hơn A[i] và L[j] lớn hơn L[jmax]
                printf("i=%d,j=%d,jmax=%d,a[%d]>a[%d] &&L[%d]>L[%d]:\n", i, j, jmax, j, i, j, jmax);
                jmax = j;  // Cập nhật jmax bằng j
                printf("jmax=j=%d\n", j);  // In giá trị cập nhật của jmax
            }
        }
        L[i] = L[jmax] + 1;  // Cập nhật giá trị của L[i]
        printf("L[%d]=L[%d]+1=%d\n", i, jmax, L[jmax] + 1);  // In giá trị cập nhật của L[i]
        T[i] = jmax;  // Gán jmax vào T[i]
        printf("T[%d]=jmax=%d\n", i, jmax);  // In giá trị cập nhật của T[i]
    }

    cout << L[0] - 2 << endl;  // In ra độ dài của dãy con tăng dài nhất

    // Truy vết và in ra dãy con tăng dài nhất
    int k = T[0];  // Bắt đầu từ vị trí đầu tiên trong T
    while(k != n + 1) {  // Duyệt đến khi k bằng n+1
        printf("a[%d]=%d;", k, A[k]);  // In ra phần tử tại vị trí k
        k = T[k];  // Cập nhật k bằng T[k]
    }
    cout << endl;

    return 0;
}