lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
# Gộp lại thành [1, 2, 3, 4, 5]

list_merge = []

for i in lst1 + lst2:
    if i not in list_merge:
        list_merge.append(i)
print(list_merge)