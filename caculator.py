import time 

def input_slow(prompt , delay = 0.05):
    for i in prompt:
        print(i , end = '' , flush = True)
        time.sleep(delay)
    return input()

def print_slow(text , delay = 0.05):
    for i in text:
        print(i , end = '' , flush = True)
        time.sleep(delay)
    print()
    
def caculator():
    print_slow("Nhập số thứ nhất: ")
    num1 = float(input_slow(""))
    print_slow("Nhập số thứ hai: ")
    num2 = float(input_slow(""))
    print_slow("Nhập phép tính: ")
    phep_tinh = input_slow("")

    if phep_tinh == "+":
        print(num1 + num2)
    elif phep_tinh == "-":
        print(num1 - num2)
    elif phep_tinh == "*":
        print(num1 * num2)
    elif phep_tinh == "/":
        print(num1 / num2)
    else:
        print("Phép tính không hợp lệ")

caculator()
