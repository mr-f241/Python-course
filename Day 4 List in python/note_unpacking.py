# 📌 Python: Ghi chú về unpacking với dấu *

# ✅ Dùng * để gom phần còn lại của danh sách vào 1 biến (dạng list)

# Ví dụ cơ bản:
numbers = [1, 2, 3, 4, 5, 6]
*mot, nam, sau = numbers
# mot  = [1, 2, 3, 4]
# nam  = 5
# sau  = 6

# ⚡ ỨNG DỤNG THỰC TẾ:

# 1. Tách phần đầu và nội dung còn lại
data = ["Tiêu đề", "dòng 1", "dòng 2", "dòng 3"]
title, *body = data
# title = "Tiêu đề"
# body  = ["dòng 1", "dòng 2", "dòng 3"]

# 2. Xử lý log (log file / CSV line)
log = ["2025-07-14", "ERROR", "File not found", "/path/to/file"]
date, level, *message = log
# date    = "2025-07-14"
# level   = "ERROR"
# message = ["File not found", "/path/to/file"]

# 3. Tách đầu, giữa, cuối
data = [1, 2, 3, 4, 5, 6]
first, *middle, last = data
# first  = 1
# middle = [2, 3, 4, 5]
# last   = 6

# 4. Truyền danh sách vào hàm với *
def tinh_tong(a, b, c):
    return a + b + c

ds = [1, 2, 3]
result = tinh_tong(*ds)  # unpack list thành từng đối số

# 5. Dùng trong vòng lặp
danh_sach = [
    ["Nam", 25, "Dev", "Hà Nội"],
    ["Mai", 30, "Designer", "Đà Nẵng"],
]

for ten, tuoi, *con_lai in danh_sach:
    print(ten, tuoi, con_lai)
# Output:
# Nam 25 ['Dev', 'Hà Nội']
# Mai 30 ['Designer', 'Đà Nẵng']

# ⚠️ Chỉ dùng được 1 dấu * khi unpack list
