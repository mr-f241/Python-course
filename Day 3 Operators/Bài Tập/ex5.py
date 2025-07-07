'''
Phân loại học lực dựa trên điểm trung bình
Nhập 3 điểm (toán, văn, anh). Tính trung bình và phân loại:

=8: Giỏi

=6.5: Khá

=5: Trung bình

<5: Yếu
'''

# Nhập điểm các môn
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))

# điểm trung bình : average score
average_score = (toan + van + anh) / 3

# Phân loại học lực

if average_score >= 8:
    print(f"Điểm trung bình là {average_score:.2f}. Học lực: Giỏi")
elif average_score >= 6.5:
    print(f"Điểm trung bình là {average_score:.2f}. Học lực: Khá")
elif average_score >= 5:
    print(f"Điểm trung bình là {average_score:.2f}. Học lực: Trung bình")
else:
    print(f"Điểm trung bình là {average_score:.2f}. Học lực: Yếu")
