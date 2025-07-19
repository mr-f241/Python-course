# Sửa đổi danh sách 
name = ['Tiến', 'Trân' , 'Hồng Tỷ' ,'Thành' , 'Tuấn']
# Thay tên đầu bằng trân và in ra tên ban đầu 
first_name = name[0]
name[0] = 'Trân'
print(f"Tên ban đầu là {first_name} đã đổi thành : {name[0]}")
# Thay tên cuối bằng tên input 
last_name = name[-1]
name[-1] = input("Nhập tên bạn muốn thay : ")
print(f"Tên ban đầu là {last_name} sau khi thay là : {name[-1]}")
# Danh sách tên sau khi đổi là 
print(name)
if 'Trân' or 'Thành' in name:
    print("A di đà phật")
else:
    print("Cút")
    