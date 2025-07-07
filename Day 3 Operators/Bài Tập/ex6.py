# Bài 6 : Kiểm tra một số nằm trong khoảng 10 đến 50 hay không sử dụng phép so sánh và logic toán tử and.

number = int(input("Nhập vào một số nguyên: "))

if number >= 10 and number <= 50:
    print(f"Số {number} nằm trong khoảng 10 -> 50")
else:
    print(f"Số {number} nằm ngoài khoảng 10 -> 50")