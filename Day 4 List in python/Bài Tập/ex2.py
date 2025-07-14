# Tìm phần tử lớn nhất và nhỏ nhất

lst = [10, 22, 5, 95, 65, 80]
max = lst[0]

for i in lst:
    if max < i:
        max = i

print(f"Max của danh sách là : {max}")