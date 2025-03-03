def TinhTongChan(lst):
    tong = 0
    for i in lst:
        if i % 2 == 0:
            tong += i
    return tong

# Nhap danh sach tu ban phim duoi dang chuoi cac so, cach nhau boi dau cach
lst = list(map(int, input("Nhap cac phan tu cua danh sach (cach nhau boi dau cach): ").split()))

# Tinh tong cac phan tu chan trong danh sach
print("Tong cac phan tu chan trong danh sach la:", TinhTongChan(lst))