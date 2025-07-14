lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: list_chan = [...], list_le = [...]
list_chan = []
list_le = []

for item in lst:
    if item % 2 != 0:
        list_le.append(item)
    else:
        list_chan.append(item)

print(f"List_chan = {list_chan} \n List_le = {list_le}")