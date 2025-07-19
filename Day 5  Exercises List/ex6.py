# Khai báo một biến danh sách có tên là it_companies và gán các giá trị ban đầu là Facebook, Google, Microsoft, Apple, IBM, Oracle và Amazon.
# banner = """

# ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗
# ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║  ██║
#    ██║   ███████║███████║██╔██╗ ██║███████║
#    ██║   ██╔══██║██╔══██║██║╚██╗██║██╔══██║
#    ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██║
#    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                           

# """

# print(banner)
it_companies = ['Facebook' , 'Google' , 'Microsoft' , 'Apple' , 'IBM' , 'Oracle' , 'Amazone']
# print(f"Danh sách công ty : {it_companies} \n")
# print(f"Số lượng công ty trong danh sách là : {len(it_companies)} \n")
# print(f"Tên công ty đầu tiên là : {it_companies[0]}\n")
# it_companies[0] = 'FB'
# print(f"Danh sách công ty sau khi sửa đổi : {it_companies}\n")
# it_companies.append("CNTT")
# print(f"Danh sách công ty sau khi cập nhật : {it_companies}\n")
# # Chèn 1 công ty vô giữa danh sách 
# midlle = len(it_companies) // 2
# it_companies.insert(midlle , "Vina")
# print(f"Danh sách sau khi chèn : {it_companies} \n")
# # Dổi tên một trong các tên công ty thành chữ in hoa 
# it_companies[1] = it_companies[1].upper()
# print(f"Danh sách sau khi in hoa {it_companies[1]} là : {it_companies}\n")
# # Nối bằng chuỗi '#;'
# it_companies2 = '#;'
# joined_string = '#;'.join(it_companies)
# print(f"Danh sách sau khi nối : {joined_string}\n")
# # Kiếm tra xem công ty nào đó có tồn ại trong danh sách 
# # nhap = input("Nhập tên công ty bạn muốn kiểm tra : ")
# # it_lower = [c.lower() for c in it_companies]
# # index_ds = it_lower.index(nhap)
# # if nhap in it_lower:
# #     print(f"Công ty {nhap} có trong danh sách ở vị trí thứ : {index_ds}")
# # else:
# #     print("Không tồn tại!!")
# # Sắp xếp danh sách bằng phương thúc sort
# it_companies.sort()
# print(f"Danh sách sau khi sắp xếp la : {it_companies}")
# # Đảo ngược 
# it_companies.reverse()
# print(f"Danh sách sau khi sắp xếp la : {it_companies}")
# # Cắt bỏ 3 công ty đầ khỏi danh sách 3: có nghĩa là lấy từ 3 đến hết danh sách
# it_companies = it_companies[3:]
# print(f"Danh sách sau kh loại bỏ 3 công ty đầu : {it_companies}")
# xóa 3 phần tử cuối
del it_companies[-3:]
print(f"Danh sách sau kh xóa 3 công ty cuối : {it_companies}")
# Loại bỏ công ty ở giữa khỏi danh sách
del it_companies[len(it_companies) // 2]
print(f"Danh sách sau khi xóa 1 công ty ở giữa : {it_companies}")
# Xóa tất cả công ty khỏi danh sách 
it_companies.clear()
print(f"Danh sách sau khi xóa tất cả công ty : {it_companies}")
# Hủy danh sách công ty 
it_companies = []
print(f"Danh sách sau khi hủy : {it_companies}")
# Tham gia vào các danh sách
it_companies = ['Facebook' , 'Google' , 'Microsoft' , 'Apple' , 'IBM' , 'Oracle' , 'Amazone']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
it_companies.extend(front_end + back_end)
print(f"Danh sách sau khi tham gia : {it_companies}")
# Sau khi nối các danh sách trong câu hỏi 26. Sao chép danh sách đã nối và gán nó cho biến full_stack, sau đó chèn Python và SQL sau Redux.
full_stack = front_end.copy()
full_stack.append('Python')
full_stack.append('SQL')
full_stack.insert(2, 'Redux')
print(f"Danh sách full_stack : {full_stack}")