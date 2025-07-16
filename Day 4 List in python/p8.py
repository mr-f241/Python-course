# Xóa các mục khỏi danh sách 
name = ['Thành' , 'Trân' , 'Nam' , 'Tiến' , 'Thảo Vy']
# Không nên xóa phần tử trong lúc đang for i in list → dễ bị bỏ sót
# Giải pháp:
# 1. Duyệt trên bản sao: list[:]
# 2. Dùng list comprehension
# 3. Duyệt ngược bằng index
for i in name[:]:
    if i != 'Thành' and i != 'Trân':
        name.remove(i)
        print(name)

# Xóa bằng pop
'''
Xóa xong trả lại phần tử đó

Nếu không có chỉ số → xóa cuối danh sách

Gây lỗi IndexError nếu chỉ số không hợp lệ
'''
print()
a = ['a' , 'b' , 'c']
x = a.pop(2)
print(x)
print(a)
# Xóa bằng del
'''
del list[index]      # Xóa phần tử theo chỉ số
del list[start:end]  # Xóa nhiều phần tử theo range
del list             # Xóa cả biến list khỏi bộ nhớ
'''
name = ['Thành' , 'Trân' , 'Nam' , 'Tiến' , 'Thảo Vy']
del name[0]
print(name)
# clear() -> xóa toàn bộ phần tử , giữ lại list rỗng
name.clear()
print(name)