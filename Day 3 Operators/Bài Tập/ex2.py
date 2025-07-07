# Bài 2 : Nhập một số nguyên. Sử dụng toán tử % để kiểm tra số đó là chẵn hay lẻ.

number =  int(input("Nhập một số nguyên: "))

if number % 2 == 0:
    print(f"Số {number} là số chẵn.")
else:
    print(f"Số {number} là số lẻ.")