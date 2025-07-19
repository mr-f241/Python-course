# Kiểm tra tập con sd issubset()
st1 = {"item1" , "item2" , "item3" , "item4"}
st2 = {"item3" , "item2"}

print(f"Kiểm tra xem s1 có phải tập con của 2 : {st1.issubset(st2)}")
print(f"Kiểm tra xem s2 có phải con của tập 1 : {st2.issubset(st1)}")