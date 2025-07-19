# Danh sách 10 học sinh theo độ tuổi 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sắp xếp danh sách và tìm độ tuổi tối thiểu và độ tuổi tối đa 

#Sắp xêp
ages.sort()
print(f"Danh sách sau khi sắp xếp là : {ages}")
# Độ tuổi tối thiểu : minimum age ; Độ tuổi tối đa : maximum
# Cách 1
minximum = ages[0]
maximum_age = ages[0]
for i in ages:
    if i < minximum:
        minximum = i
    if i > maximum_age:
        maximum_age = i
ages.append(minximum)
ages.append(maximum_age)
print(f"Độ tuổi tối thiểu là : {minximum}")
print(f"Độ tuổi tối đa là : {maximum_age}")
print(f"Danh sách sau khi thêm là : {ages}")
# # Cách 2 :
# print(f"Độ tuổi tối thiểu là {min(ages)}")
# print(f"Độ tuổi tối đa là : {max(ages)}")

# 