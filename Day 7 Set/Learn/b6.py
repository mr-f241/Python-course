number = {1 , 2 , 3}
# Tham gia tập hợp 
# Cách 1 sử dụng union 
number2 = {11 , 12, 13}
# number3 = number.union(number2)
# print(f"Tham gia tập hợp bằng union : {number3}")
# cách 2 : Sử dụng hàm update
number.update(number2)
print(f"Tham gia tập hợp bằng update : {number}")