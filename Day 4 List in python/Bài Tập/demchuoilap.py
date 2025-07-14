# Tìm phần tử xuất hiện nhiều nhất trong list.
lst = [2, 3, 2, 5, 4, 2, 3, 5]

max_count = 0
most_common = None

for i in lst:
    count = lst.count(i)
    if count > max_count:
        max_count = count
        most_common = i

print(f"Phần tử xuất hiện nhiều nhất là: {most_common} ({max_count} lần)")
