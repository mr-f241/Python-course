# --- Ghi chú về tuple và set trong Python ---

# Tuple: Là kiểu dữ liệu có thứ tự, không thể thay đổi (immutable), cho phép phần tử trùng lặp.
# - Khai báo bằng dấu ngoặc tròn ()
# - Ví dụ: tup = (1, 2, 3)
# - Nếu tuple chứa object có thể thay đổi (như list), thì nội dung object đó vẫn thay đổi được.

# Set: Là kiểu dữ liệu không có thứ tự, không chứa phần tử trùng lặp, có thể thay đổi (mutable).
# - Khai báo bằng dấu ngoặc nhọn {} hoặc hàm set()
# - Ví dụ: s = {1, 2, 3}
# - Không truy cập phần tử theo chỉ số, không cho phép phần tử trùng lặp.

# '''
# +set 
# +tuple
# '''
# # Tuple trong Python là immutable (không thể thay đổi giá trị sau khi tạo). Bạn không thể thay đổi, thêm, xóa phần tử trực tiếp trong tuple.
# # Tuple nhiều phần tử
# tup1 = (1, 2, 3, 4, 5)

# # Tuple một phần tử (phải có dấu phẩy)
# tup2 = (1,)

# # Tuple rỗng
# tup3 = ()

# # Tuple chứa nhiều kiểu dữ liệu
# tup4 = (1, "Python", 3.14, True)

# # Tuple lồng nhau (nested tuple)
# tup5 = (1, (2, 3), [4, 5])
# # Tuple không cần ngoặc nếu dùng trong phép gán
# tup6 = 1, 2, 3

# print(tup1)  # In ra: (1, 2, 3, 4, 5)
# print(tup2)  # In ra: (1,)
# print(tup3)  # In ra: ()
# print(tup4)  # In ra: (1, 'Python', 3.14, True)
# print(tup5)  # In ra: (1, (2, 3), [4, 5])
# print(tup6)  # In ra: (1, 2, 3)

# Set
# set1 = set()  # Tạo một set rỗng

# set1.add(1)  # Thêm phần tử 1 vào set
# set1.update([2, 2, 4])  # Thêm nhiều phần tử vào set
# set1.remove(2)  # Xóa phần tử 2 khỏi set
# set2 = set1.copy()  # Sao chép set1 sang set2

# print(set1 is set2)  # Kiểm tra xem set1 và set2 có giống nhau không (False)

# Các kiểu dữ liệu set()
# set1 = {}
# set2 = set()  # Tạo một set rỗng
# print(type(set1))  # In ra: <class 'dict'> (set1 là dict rỗng)
# print(type(set2))  # In ra: <class 'set'> (set2 là set rỗng)

