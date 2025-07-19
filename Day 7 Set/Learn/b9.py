'''
issuperset() là hàm trong Python dùng để kiểm tra xem một tập hợp (set) 
 có phải là tập cha (tập bao) của một tập hợp khác hay không.
'''
a = {1 ,2, 3, 4, 5, 6, 7, 8,9 , 10}
b = {5 , 6, 3, 1, 2}
print("A có phải là tập bao của B : ", a.issuperset(b))
print("B có phải là tập bao của A : ", b.issuperset(a))
# Kiểm tra sự khác biệt giữa hai tập hợp
c = a.difference(b)
print(f"Sự khác biệt giữa a và b là : {a.difference(b)}")
print("Sự khác biệt giữa b và a là : ", b.difference(a))
print("Bạn có muốn gán a vô b để bù đắp khuyết điểm nây")
input_ans = input("Y/N : ")
if input_ans.lower() == "y":
    b.update(c)
    print("B sau khi gán : ", b)
