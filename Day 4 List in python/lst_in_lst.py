'''
+List in list in Python
+Copy list 
+list slicing
# +List comprehension

'''
# Gán list cho biến khác (lst2 = friends) thì cả hai cùng tham chiếu 1 list.
# Thay đổi lst2 thì friends cũng thay đổi (và ngược lại).
# Các hàm như append(), sort(), reverse() thay đổi list tại chỗ và trả về None nếu gán cho biến khác.
# Muốn copy list độc lập thì dùng friends.copy() hoặc friends[:]

# friends = [["Thành" , 2006] , ["Hùng" , 2005], ["Hải" , 2004]]
# friends.append(["Hà" , 2003])
# lst2 = friends
# print(lst2)

a = [1 , -3 , 5 , 0 , 9 ,7]
print(a[::-1]) # In ra list đảo ngược

print(id(a)) # In ra id của list a

# [giá trị_muốn_thêm for phần_tử in danh_sách if điều_kiện]
# vd [x for x in lst if x % 2 == 0]
