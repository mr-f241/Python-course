lst = [1, 2, 2, 3, 4, 4, 5]
# Tạo list mới không chứa phần tử trùng lặp
a = []

for i in lst: # Duyệt qua từng phần tử trong danh sách 
    if i not in a: #Nếu mà nó không có trong list rông thì gán vô còn có thì thôi
       a.append(i)

print(a)