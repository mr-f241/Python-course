# Cắt các mục từ danh sách
# Cú pháp slicing trong python 
# list[start:end]
# start : chỉ mục bắt đầu bao gồm ; end : không bao gồm phần từ tạo vitri này
# vd list[0:4] --> nó sẽ in từ 0 -> 3
'''
📌 Ghi nhớ mẹo:
::step → nhảy theo bước
start::step → bắt đầu từ đâu, nhảy theo bước và nó sẽ nhảy đến khi hết
::2 → lấy cách nhau 1 phần tử
::1 → lấy toàn bộ
[::-1] → đảo ngược danh sách
'''
name = ['Tiến', 'Trân' , 'Hồng Tỷ' ,'Thành' , 'Tuấn']
# Chỉ mục dương
print('='*80)
print("IN RA CHỈ MỤC DƯƠNG")
print(f"\nIn ra tất cả tên : {name[0:5]}")
print(f"In ra tất cả tên : {name[:]}")
print(f"In ra tên cuối cùng : {name[-1]}")
print(f"In ra tên từ 0->2: {name[:3]}")
print(f"In ra tên đầu với tên thứ 3 : {name[::3]}")
print(f"In ra tên Trân với Thành {name[1::2]} \n") #Nhảy 1 -> 3 -> 5 mà 5 không có nên dưng tại 3 và in ra mình 3
print('='*80)
print("\nIN RA CHỈ MỤC ÂM")

print(f"In ra từ -5 đến hết toàn bộ danh sách : {name[-5:]}")
print(f"In ra từ Trân Thành : {name[-4:-1]}")
print(f"In ra Trân và Thành : {name[-4::2]}") #Bước nhảy luôn dương

