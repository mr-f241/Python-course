# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr)
# print(fr)
# print(bg)
# print(scandic)
# print(sw)
# print(es)
# ----------Danh sách giải nén------------------
lst = ['Thành' , 'Trân' , 'Vy' , 'Tuyến' , 'Linh']

*ny , nyc1 , nyc2 , nyc3 = lst

# print(f"Ny của bạn là : {[char for char in ny[1]]}")
print(f"Tên ny của bạn là : {ny[1]}")
print(f"Tên của nyc thứ nhất : {nyc1}")
print(f"Tên của nyc thứ hai : {nyc2}")
print(f"Tên của nyc thứ ba : {nyc3}")