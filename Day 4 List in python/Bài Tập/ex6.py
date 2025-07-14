lst = [10, 20, 30, 40, 50]
# Tính giá trị trung bình
# Cách 1 : 
# total = 0
# print(len(lst))
# for i in lst:
#     total = (total + i)

# average = total / len(lst)
# print(f"Trung bình cộng của danh sách là : {average}")

# Cách 2:

average = sum(lst) / len(lst)
print(average)