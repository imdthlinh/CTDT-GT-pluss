def cai_tui(n, w, A, C):
    #Sắp xếp đồ vật theo tt giảm dần:
    items = sorted(zip(C, A), reverse=True)

    total_value = 0
    selected_items = []
    current_weight = 0

    for value, weight, in items:
       if current_weight + weight <= w:
            # Thêm đồ vật vào túi
            total_value += value
            selected_items.append((weight, value))
            current_weight += weight

    # Trả về kết quả
    return total_value, selected_items

n, w = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

total_value, selected_items = cai_tui(n, w, A, C)
total_weight = sum([weight for weight, value in selected_items])

print(f"Tong trong luong ={total_weight}")
print(f"Tong gia tri ={total_value}")

#tạo danh sách để lưu thứ tự các đồ vật đã được chọn
selected_order = []
for i, (weight, value) in enumerate(selected_items):
    # Tìm chỉ số của đồ vật hiện tại trong danh sách đầu vào
    for j, (w, v) in enumerate(zip(A, C)):
        #check cặp gt,kl hiện tại có khớp với cặp giá trị, kl trong ds ban đầu ko
        if weight == w and value == v: 
            selected_order.append(j + 1)
        #thêm chỉ số của đồ hiện tại (trong ds đầu vào) vào ds select_ord
            break

# In danh sách các đồ vật được chọn theo thứ tự đã được sắp xếp
for i, order in enumerate(selected_order):
#lấy cặp gt,kl tương ứng với thứ tự hiện tại trong sl_ord
    weight, value = selected_items[i]
    print(f"{order}({weight},{value})", end=";")
