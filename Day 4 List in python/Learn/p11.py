# Phương thức count() trả về số lần một mục xuất hiện trong danh sách
lst = [1, 2, 3, 1, 2, 1]
lst.count(1)
print("Số lần xuất hiện của 1 trong danh sách là: ", lst.count(1))

# Phương thức index trả về chỉ mục của một mục trong danh sách tức là tìm vị trí mà số đó xuất hiện

name = ['Thành', 'Trân' , 'Nam']
print(name.index('Nam'))
print(f"Vị trí của Trân trong danh sách là : {name.index('Trân')}")

# Đảo ngược danh sách
# Lưu ý reverse() chỉ thay đổi list gốc không trả về list mới 
# print(lst.reverse())  # In ra None nên thay đổi trước in ra sau
lst.reverse()
print(f"Danh sách sao khi đảo ngược là : {lst}")

# Sắp xếp danh sách bằng sort()
# Lưu ý nếu sort() sắp xếp tắng dần còn sort(reverse = True) sắp xếp giảm dần
lst.sort()
print("Danh sách list sắp xếp tắng dần:", lst)
lst.sort(reverse = True)
print(f"Danh sách list sắp xếp theo thứ tự giảm dần là : {lst}")

# Sorted() trả về danh sách đã sắp xếp mà không sủa đổi danh sách gốc 
'''
Hiểu đơn giản thì nó giông như sort nm sắp xếp trên danh sách copy
ds = [1 ,2,3,4,5]
new_ds = ds.copy()
print(new_ds.sort(reverse = True))
'''
ds = [1 , 2, 3, 4, 5]
new_lst = sorted(ds , reverse = True)
print(f"List ban đầu : {ds} sau khi sắp xếp theo thứ tự giảm dần là : {new_lst}")