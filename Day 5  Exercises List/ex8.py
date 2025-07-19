ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Tìm độ tuổi trung bình (một mục ở giữa hoặc hai mục ở giữa chia cho hai)
ages.sort()
n = len(ages)
if n % 2 != 0:
    median = ages[n//2]
else:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2
print(f"Tuổi trung bình là : {median}")