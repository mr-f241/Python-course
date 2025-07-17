# Nối danh sách
# cách 1 : Sử dụng toán tử +
lst1 = ['Thành']
icon_heart = ['❤️']
lst2 = ['Trân']
love = lst1 + icon_heart + lst2
print(love)

# Cách 2 : extend 
'''
nó chỉ có thể nối một list vào list gốc  nếu muốn thêm thì lại nối thêm một cái mói 
vd : lst.extend(lst2) 
lst1.extend(lst3)
hoặc kết hợp 
với toán tử cộng lst1.extend(lst2 + lst3)
'''
last_name = ['Thành']
first_name = ['Trần']
age = [18]
last_name.extend(first_name)
last_name.extend(age)
print(last_name)