import time
# Bài tập về xóa , thêm , dọn , chèn 
name = ['thành' , 'trân' , 'nam' , 'tiến']
def print_slow(text , delay=0.03):
    for char in text:
        print(char , end='' , flush=True)
        time.sleep(0.03)
    print()
print_slow("╔══════════════════════════════════════╗")
print_slow("║     📋 MENU QUẢN LÝ DANH SÁCH        ║")
print_slow("╠══════════════════════════════════════╣")
print_slow("║  1.➕  Thêm tên                      ║")
print_slow("║  2.🗑️ Xóa tên                       ║")
print_slow("║  3.📌  Chèn tên vào vị trí cụ thể    ║")
print_slow("║  4.🧹 Dọn sạch danh sách            ║")
print_slow("║  5.👀  Hiển thị danh sách            ║")
print_slow("║  0.❌  Thoát chương trình            ║")
print_slow("╚══════════════════════════════════════╝")


while True:
    choice = input("Nhập vào lựa chọn của bạn :")
    if choice == '1':
        add_name = input("Nhập tên bạn muốn thêm vào danh sách : ")
        name.append(add_name)
        print_slow(f"✅ Danh sách sau khi thêm là : {name}")
    elif choice == '2':
        to_remove = []
        number = int(input("Nhập số lượng tên bạn muốn xóa : "))
        for i in range(number):
            rm_name = input(f"Nhập tên thứ {i+1} : ")
            to_remove.append(rm_name)
        
        for name_to_remove in to_remove:
            if name_to_remove in name:
                name.remove(name_to_remove)
                print(f"✅Đã xóa |{name_to_remove}| khỏi danh sách")
            else:
                print_slow(f"❌ Không tìm thấy '{name_to_remove}' trong danh sách.")

        print_slow(f"📋 Danh sách sau khi xóa: {name}")
    elif choice == '3':
        insert_name = input("Nhập vào tên bạn muốn chèn : ")
        try:
            location_name = int(input("Nhập vị trí bạn muốn chèn: "))
            if 0 <= location_name <= len(name):
                name.insert(location_name, insert_name)
            else:
                print_slow("⚠️ Vị trí không hợp lệ.")
        except ValueError:
            print_slow("⚠️ Vui lòng nhập một số.")
        # insert(vị trí , thứ muốn chèn)
        print_slow(f"✅List sau khi chèn {insert_name} là : {name}")
    elif choice == '4':
        name.clear()
        print_slow(f"✅List sau khi dọn dẹp : {name}")
    elif choice == '5':
        print_slow(f"✅List ban đầu của bạn là : {name}")
    elif choice == '0':
        print_slow("Tạm biệt😥😥")
        break
    else:
        print_slow("Vui lòng nhập lại 🔙")
        
       
        
    