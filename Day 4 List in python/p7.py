# Chàn các mục vào danh sách 
# list.insert(vị_trí, giá_trị)
# Làm màu
import time
def print_slow(text , delay = 0.05):
    for char in text:
        print(char , end='' , flush=True)
        time.sleep(0.05)
    print()
# Danh sách ban đầu
name = ['Thành' , 'Trân' , 'Hồng Tỷ' , 'Nam' , 'Tiến']
# Nhập vào vị trí và giá trị cần chèn
location = int(input("Nhập vị trí bạn muốn chèn : "))
list_insert = input("Nhập vào chuỗi bạn muốn chèn vào danh sách : ")
# Chèn : insert
name.insert(location , list_insert)
# in ra mọi thứ
print_slow(f"Đã chèn {list_insert} vào vị trí {location} danh sách sau khi chèn là : \n{name}")