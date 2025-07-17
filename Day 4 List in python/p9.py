# Sao chép danh sách
'''
Có thể sao chép một danh sách bằng cách gán lại nó cho một biến mới theo cách sau: list2 = list1. Bây giờ, list2 là một tham chiếu của list1, bất kỳ thay đổi nào chúng ta thực hiện trên list2 cũng sẽ sửa đổi bản gốc, list1. Tuy nhiên, có rất nhiều trường hợp chúng ta không muốn sửa đổi bản gốc mà muốn có một bản sao khác. Một trong những cách để tránh vấn đề trên là sử dụng copy() .
'''
# lst1 = [1, 2, 3, 4, 5]
# lst2 = lst1 # lst2 là một tham chiếu của lst1
# lst2.remove(1) # Xóa phần tử 1 khỏi lst2
# print(lst1) #lst1 cũng bị thay dổi

lst1 = [1, 2, 3, 4, 5]
lst2 = lst1.copy() # Sao chép list
lst2.remove(1) # Xóa phần tử 1 khỏi lst2
print(lst1) #lst1 không bị thay dổi