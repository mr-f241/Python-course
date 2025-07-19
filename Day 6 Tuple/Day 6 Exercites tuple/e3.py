# Tạo các bộ dữ liệu trái cây, rau củ và sản phẩm động vật. Nối ba bộ dữ liệu này lại và gán nó vào một biến có tên là food_stuff_tp.
fruit = ('Táo' , 'Chuối' , 'Lê' , 'Ổi' , 'Mận')
vegetables = ('Muống' , 'Cải' , 'Cần' , 'Su su' , 'Bí')
animal_products = ('Mỡ heo' , 'Ba chỉ nổ bì' , 'Lòng lợn')
food_stuff_tp = fruit + vegetables + animal_products
print(food_stuff_tp)
#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))
# Cắt bỏ phần ử ở giữa
del_middle_element = len(food_stuff_lt) // 2 # Lấy phần tử ở giữa
middle_value = food_stuff_lt[del_middle_element] #Lưu giá trị ở giữa
del food_stuff_lt[del_middle_element] # Xóa phần tử ở giũa
print(f"List sau khi xóa phần ử ở giữa : {food_stuff_lt}") #Phần tử sau khi xóa
print(f"Chuỗi ở giữa là : {middle_value}") #In ra phần tủ ở giữa

# Cắt bỏ 3 phần tử đầu cuối
food_stuff_lt = food_stuff_lt[3:]
print(f"List sau khi xóa 3 phần tử đầu : {food_stuff_lt}")

# Xóa 3 phần tử cuối
del food_stuff_lt[-3:]
print(f"List sau khi xóa 3 phần tử cuối : {food_stuff_lt}")

# Xóa hoàn toàn tuple food_staff_tp 
food_stuff_tp = ('Táo' , 'Chuối' , 'Lê' , 'Ổi' , 'Mán')
# del food_stuff_tp
'''
Các cách xóa từng phần tử trong tuple gốc 
✅ Có thể del biến hoặc gán lại tuple mới nếu muốn “xóa”.
✅ Chuyển sang list nếu muốn thao tác kiểu thêm/xóa.
'''
# Xóa bằng cách chuyển qua list
food_list = list(food_stuff_tp)
del food_list[1]
food_staff_tp = tuple(food_list)
print(f"Tuple sau khi xóa : {food_staff_tp}")
