# Nhap danh sach tu ban phim duoi dang chuoi cac so, cach nhau boi dau cach
lst = list(map(int, input("Nhap cac phan tu cua danh sach (cach nhau boi dau cach): ").split()))

# Tao tuple tu danh sach
tup = tuple(lst)

# Truy cap phan tu dau tien va cuoi cung trong tuple
print("Phan tu dau tien trong tuple la:", tup[0])
print("Phan tu cuoi cung trong tuple la:", tup[-1])
