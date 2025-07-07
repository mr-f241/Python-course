# Bài 3 : Nhập năm sinh. Dùng toán tử - để tính tuổi hiện tại (giả sử năm hiện tại là 2025).

year_of_birth = int(input("Nhập năm sinh của bạn: "))
current_year = 2025 # current year :  năm hiện tại
age = current_year - year_of_birth

print(f"Tuoi cua ban la {age} tuoi.")