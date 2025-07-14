# # Cho list số nguyên, kiểm tra xem có phần tử nào trùng nhau không.
# lst = [1,2,3,5,1]
# dem = False
# for i in lst:
#     if lst.count(i) > 1:
#         dem = True
#         break
# if dem:
#     print("Có phần tử trùng nhau.")
# else:
#     print("Không có phần tử trùng nhau.")

# Cách 2
# Cho list số nguyên, kiểm tra xem có phần tử nào trùng nhau không.
lst = [1 , 3,2,5, 6, 7,2]

trung = set([i for i in lst if lst.count(i) > 1])

if trung:
    print("Trùng")
else:
    print("Không Trùng")