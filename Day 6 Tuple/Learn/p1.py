'''
Tuple là tập hợp các kiểu dữ liệu khác nhau, được sắp xếp theo thứ tự và không thể thay đổi (immutable).
Tuple được viết bằng cặp ngoặc tròn (). Sau khi một tuple được tạo, chúng ta không thể thay đổi giá trị của nó. 
Chúng ta không thể sử dụng các phương thức add, insert, remove trong tuple vì nó không thể sửa đổi (mutable). 
Không giống như danh sách, tuple có ít phương thức. Các phương thức liên quan đến tuple:

tuple(): để tạo một tuple rỗng
count(): để đếm số lượng mục được chỉ định trong một bộ
index(): để tìm chỉ mục của một mục được chỉ định trong một bộ
toán tử: để nối hai hoặc nhiều bộ và tạo một bộ mới
'''
name = ('Vip' , 'Pro' , 'Code')
print(name[len(name) - 1])
# Chuyển đổi thành list
print(list(name))
# Cắt lát 
# 0 -> 2 in ra 0 -> 1
print(name[0 : 2])
# Xóa dũ liệu 
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
print()