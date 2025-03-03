def daoNguocDanhSach(lst):
    # Su dung cach slicing de dao nguoc danh sach
    return lst[::-1]

# Nhap danh sach tu ban phim duoi dang chuoi cac so, cach nhau boi dau cach
lst = list(map(int, input("Nhap cac phan tu cua danh sach (cach nhau boi dau cach): ").split()))

# Dao nguoc danh sach
lst_dao_nguoc = daoNguocDanhSach(lst)

print("Danh sach sau khi dao nguoc:", lst_dao_nguoc)
