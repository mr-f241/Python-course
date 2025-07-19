name = {"Thành" , "Trần" , "Hồng Tỷ"}
# Xoa các mục khỏi tập hợp
name.remove("Hồng Tỷ")
print("Set sau khi xóa : ", name)
# Xóa ngẫu nhiên và trả về mục đã xóa pop
delete = name.pop()
print("Phần tử đã bị xóa khỏi set : ", delete)
# Dọn sạch trả về set
name.clear()
print("Set sau khi dơn sạch : ", name)
# Xóa một tập hợp 
del name