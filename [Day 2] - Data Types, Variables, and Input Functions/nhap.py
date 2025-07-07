# input in python lưu ý input sẽ sẽ là kiểu str
# .5 trong python có nghĩa là 0.5 kiểu float
import sys

while True:
    full_name = input("Nhập tên của bạn: ")
    print(type(full_name))
    if "thành" in full_name.lower():
        print("Nhập tên tao làm gì?")
    else:
        print("Hello " + full_name)
        break
