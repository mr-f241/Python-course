# Bài 9 : nhập vào một năm. If chia hết cho 4 mà không chia hết cho 100 hoặc chia hết cho 400 thì là năm nhuận.

Input_year = int(input("Nhập vào một năm bất kì : "))

if (Input_year % 4 == 0 and Input_year % 100 != 0) or Input_year % 400:
    print(f"{Input_year} là năm nhuận : leap year")
else:
    print(f"{Input_year} không phải năm nhuận : not a leap year")