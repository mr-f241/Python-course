# Cách 1 dùng vòng lặp for không gây thay đổi thứ tự 
# Tạo list mới từ list cũ, nhưng chỉ chứa các phần tử không trùng lặp.
lst = [1 ,2,4 , 4,2 ,3,6,7, 8]

lst_new = []

for i in lst:
    if i not in lst_new:
        lst_new.append(i)

print(lst_new)

#Cách 2 : Sử dụng set có thể gây mất thứ tự
lst_new = list(set(lst))
print(lst_new)

#Cách 3 : dict giữ nguyên thứ tự
lst_new = list(dict.fromkeys(lst))
print(lst_new)  # [1, 2, 4, 3, 6, 7, 8]
