# Tạo một bộ tên chứa tên của chị gái và anh trai của bạn (anh chị em tưởng tượng cũng được)
import random
import time
import colorama
def print_slow(text , delay = 0.03):
    for char in text:
        print(char , end='' , flush=True)
        time.sleep(0.03)
    print()
banner = """

███████╗ █████╗ ███╗   ███╗██╗██╗  ██╗   ██╗
██╔════╝██╔══██╗████╗ ████║██║██║  ╚██╗ ██╔╝
█████╗  ███████║██╔████╔██║██║██║   ╚████╔╝ 
██╔══╝  ██╔══██║██║╚██╔╝██║██║██║    ╚██╔╝  
██║     ██║  ██║██║ ╚═╝ ██║██║███████╗██║   
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚═╝   

"""
print_slow(banner)
sisters = ('Chí', 'Anh')
brothers = ('Thành' , 'Nam')
# Kết hợp anh chị em 
siblings = sisters + brothers
# Đếm anh chị em 
number_of_siblings = len(siblings)
# Sửa đổi siblings gán nó cho family_members
# Để tránh lỗi do Hàm print_slow() của bạn chỉ nhận một đối số text nhưng ở đây có hai đối số nên:
'''
Lỗi : print_slow("Name of sisters : ", sisters)  # ❌ Gây lỗi: TypeError
Cách sửa 1 : 
print_slow("Name of sisters : " + str(sisters))
Cách sửa 2 : 
print_slow(f"Name of sisters : {sisters}")
'''
family_members = siblings + ("Bố" , "Mẹ")
print_slow("Name of sisters : " +str(sisters))
print_slow("Name of brothers : " + str(brothers))
print_slow("Name of siblings : " + str(siblings))
print_slow("Number of siblings : " +str(number_of_siblings))
print_slow(f"Family members : {family_members}")
# Giải nén anh chị em và cha mẹ từ family_members sử dụng unpacking và dấu * để gom giá trị
*siblings , dad , mom = family_members
print_slow(f"Name of siblings :  {siblings}")
print_slow(f"Name of dad : {dad}" , delay=0.01)
print_slow(f"Name of mom : {mom}")

