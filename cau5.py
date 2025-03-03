# Nhap danh sach tu ban phim duoi dang chuoi cac so, cach nhau boi dau cach
lst = list(map(int, input("Nhap cac phan tu cua danh sach (cach nhau boi dau cach): ").split()))

# Tao dictionary de luu so lan xuat hien cua moi phan tu
dem = {}

for phan_tu in lst:
    if phan_tu in dem:
        dem[phan_tu] += 1
    else:
        dem[phan_tu] = 1

print("So lan xuat hien cua moi phan tu trong danh sach la:", dem)
