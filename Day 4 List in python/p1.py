# Su ungham tich hop danh sach : Using list built-in function
# empty_list = list()
# print(len(empty_list))

# Su dung dau ngoac vuong : Using square brackets
# empty_list = []
# print(len(empty_list))
import random
last_name = ['Nguyen', 'Tran', 'Le', 'Pham', 'Hoang']
first_name = ['An', 'Binh', 'Cuong', 'Duc', 'Em']
city = ['Hanoi', 'Ho Chi Minh', 'Da Nang', 'Hai Phong', 'Can Tho' , 'Thanh Hoa' , 'Vung Tau' , 'Bac Ninh']
thongtin = []
soluong = int(input("Nhap vao so luong :"))
for i in range(soluong):
    thongtin.append(random.choice(last_name) + " " + random.choice(first_name) + " - " + random.choice(city))
    print(thongtin[i])
    