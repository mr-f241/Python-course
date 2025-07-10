numbers = [1 , 2 , 3 ,4]

# numbers.append(5)  # Thêm phần tử vào cuối danh sách
# numbers.insert(0, 0)  # Thêm phần tử vào đầu danh sách
# numbers.remove(3)  # Xóa phần tử đầu tiên có giá trị 3
# last_value = numbers.pop()  # Xóa và trả về phần tử cuối cùng trong danh sách
# print(last_value)
# numbers.sort()  # Sắp xếp danh sách theo thứ tự tăng dần
# numbers.reverse()  # Đảo ngược thứ tự của danh sách
# numbers.sort(reverse=True)  # Sắp xếp giam dần
# numbers.clear()
a = numbers.copy()  # Tạo bản sao của danh sách
# print(a.sort(reverse=True))
print(a.count(2))  # Đếm số lần xuất hiện của giá trị 2 trong danh sách
print(a.index(3))  # Trả về chỉ số của phần tử đầu tiên có giá trị 3 trong danh sách
print(numbers)