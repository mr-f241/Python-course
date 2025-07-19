number = {1 , 3 , 7, 3, 9 , 5 , 2, 0}
# Sắp xếp 
print(f"Sắp xếp tập hợp : {sorted(number)}")
new_number = sorted(number)
# sort chỉ dùng với list và thay đổi dữ liệu gốc
new_number.sort()
print(f"Sắp xếp tập hợp bằng sort : {type(new_number)}")
# Sắp xếp tập hợp bằng sorted()
print(f"Sắp xếp tập hợp bằng sorted() : {type(new_number)}")
print(type(number))