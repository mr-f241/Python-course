# Tìm kiếm các mục giao nhau trong set 
# Tìm kiếm các mục có mặt trong cả 2 set
# Cú pháp : set1.intersection(set2)
# intersection không làm thay đổi set gốc, trừ khi bạn dùng intersection_update().
st1 = {"item1" , "item2" , "item3" , "item4"}
st2 = {"item3" , "item2" , "item9"}
# print(f"Set giao nhau : {st1.intersection(st2)}")
# Ví dụ 
# cách 1 sử dụng set ở đây để tách nó thành từng kí tự nếu không sẽ dính liền
chrst1 = set(''.join(st1))
chrst2 = set(''.join(st2))
common = chrst1.intersection(chrst2)
print(f"Set giao nhau : {common}")
# cách 2 sử dụng vòng for 
char1 = set()
char2 = set()

for word in st1:
    for char in word:
        char1.add(char)

for word in st2:
    for char in word:
        char2.add(char)

common = char1.intersection(char2)
print(f"Set giao nhau : {common}")