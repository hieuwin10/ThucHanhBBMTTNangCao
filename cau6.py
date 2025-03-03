# Nhap so luong phan tu cua dictionary
n = int(input("Nhap so luong phan tu cua dictionary: "))
dict_data = {}
for i in range(n):
    key = input("Nhap key thu " + str(i+1) + ": ")
    value = input("Nhap gia tri cho key " + key + ": ")
    dict_data[key] = value

print("Dictionary truoc khi xoa:", dict_data)

# Nhap key can xoa
key_xoa = input("Nhap key can xoa: ")

# Kiem tra va xoa key neu ton tai
if key_xoa in dict_data:
    del dict_data[key_xoa]
    print("Dictionary sau khi xoa:", dict_data)
else:
    print("Key '" + key_xoa + "' khong ton tai trong dictionary.")
