def gcd(a,b):
    if b == 0:
        return a #nếu b=0 thì a là ucln(a,b)->hàm trả về a
    return gcd(b, a % b) #trường hợp ko, thì sdung đệ quy bằng cách gọi lại chính nó với tham số b và phần dư của a chia b

i = int(input()) #giá trị nhập từ người dùng với hàm input, i đại diện cho số lần lặp trong vòng while

while(i): #map():chuyển đổi các giá trị nhập vào thành các số nguyên. split():tách các giá trị nhập vào thành từng phần riêng biệt.
    a,b = map(int, input().split()) #
    print(gcd(a,b))#giá trị ucln(a,b) tính bằng cách gọi hàm 
    i-=1 #biến i giảm đi 1 sau mỗi lần lặp để đảm bảo số lần lặp ko vô hạn
