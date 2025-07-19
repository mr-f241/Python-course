# Kiểm tra xem một mục có tồn tại trong tuple không:
# Kiểm tra xem 'Estonia' có phải là một quốc gia Bắc Âu không

# Kiểm tra xem 'Iceland' có phải là một quốc gia Bắc Âu không

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print("Estonia is a Nordic country.")
elif 'Iceland' in nordic_countries:
    print("Iceland is a Nordic country.")
else:
    print("Estonia is not a Nordic country.")