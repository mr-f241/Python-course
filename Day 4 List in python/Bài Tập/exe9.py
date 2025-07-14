lst = ['python', 'java', 'c++']
# Output: ['PYTHON', 'JAVA', 'C++']

# Cách 1
lst_rong = []
for i in lst:
    lst_rong.append(i.upper())

print(lst_rong)

# Cách 2
# print([i.upper() for i in lst])