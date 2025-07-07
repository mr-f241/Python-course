'''
Bài 8: Đảo ngược giá trị 2 bằng toán tử
Nhập 2 số, sau đó thay đổi giá trị 2 biến dùng toán tử mà không sử dụng tạm thời biến.
'''

number1 = int(input("Nhập vào số thứ nhất : "))
number2 = int(input("Nhập vào số thứ hai : "))

# Đảo ngược vị trí
# Cách 1
# number1 = number1 + number2 
# number2 = number1 - number2
# number1 = number1 - number2

# print(f"Number1 = {number1} | Number2 = {number2}")

# Cách 2
number1 , number2 = number2 , number1

print(f"Number1 = {number1} | Number2 = {number2}")
