class SinhVien:
    next_id = 1  # Tự động tăng mã sinh viên

    def __init__(self, ten, gioitinh, chuyennganh, diem):
        self.id = SinhVien.next_id
        SinhVien.next_id += 1
        self.ten = ten
        self.gioitinh = gioitinh
        self.chuyennganh = chuyennganh
        self.diem = diem
        self.hocluc = self.tinh_hocluc()

    def tinh_hocluc(self):
        if self.diem >= 8:
            return "Gioi"
        elif self.diem >= 6.5:
            return "Kha"
        elif self.diem >= 5:
            return "Trung binh"
        else:
            return "Yeu"

    def cap_nhat(self, ten, gioitinh, chuyennganh, diem):
        self.ten = ten
        self.gioitinh = gioitinh
        self.chuyennganh = chuyennganh
        self.diem = diem
        self.hocluc = self.tinh_hocluc()

    def __str__(self):
        return (f"ID: {self.id}, Ten: {self.ten}, Gioi tinh: {self.gioitinh}, "
                f"Chuyen nganh: {self.chuyennganh}, Diem: {self.diem}, Hoc luc: {self.hocluc}")


def them_sinh_vien(sinh_vien_list):
    print("\n--- Them sinh vien ---")
    ten = input("Nhap ten: ")
    gioitinh = input("Nhap gioi tinh: ")
    chuyennganh = input("Nhap chuyen nganh: ")
    diem = float(input("Nhap diem trung binh: "))
    sv = SinhVien(ten, gioitinh, chuyennganh, diem)
    sinh_vien_list.append(sv)
    print("Them sinh vien thanh cong!")


def cap_nhat_sinh_vien(sinh_vien_list):
    print("\n--- Cap nhat thong tin sinh vien ---")
    id_can_cap_nhat = int(input("Nhap ID sinh vien can cap nhat: "))
    for sv in sinh_vien_list:
        if sv.id == id_can_cap_nhat:
            print("Nhap thong tin moi cho sinh vien:")
            ten = input("Nhap ten: ")
            gioitinh = input("Nhap gioi tinh: ")
            chuyennganh = input("Nhap chuyen nganh: ")
            diem = float(input("Nhap diem trung binh: "))
            sv.cap_nhat(ten, gioitinh, chuyennganh, diem)
            print("Cap nhat thong tin sinh vien thanh cong!")
            return
    print("Khong tim thay sinh vien voi ID da cho.")


def xoa_sinh_vien(sinh_vien_list):
    print("\n--- Xoa sinh vien ---")
    id_can_xoa = int(input("Nhap ID sinh vien can xoa: "))
    for i, sv in enumerate(sinh_vien_list):
        if sv.id == id_can_xoa:
            del sinh_vien_list[i]
            print("Xoa sinh vien thanh cong!")
            return
    print("Khong tim thay sinh vien voi ID da cho.")


def tim_kiem_sinh_vien(sinh_vien_list):
    print("\n--- Tim kiem sinh vien ---")
    ten_tim = input("Nhap ten sinh vien can tim: ")
    ket_qua = [sv for sv in sinh_vien_list if ten_tim.lower() in sv.ten.lower()]
    if ket_qua:
        print("Ket qua tim kiem:")
        for sv in ket_qua:
            print(sv)
    else:
        print("Khong tim thay sinh vien nao voi ten da cho.")


def sap_xep_theo_diem(sinh_vien_list):
    print("\n--- Sap xep theo diem trung binh ---")
    sinh_vien_list.sort(key=lambda sv: sv.diem, reverse=True)  # Sắp xếp giảm dần theo điểm
    for sv in sinh_vien_list:
        print(sv)


def sap_xep_theo_chuyen_nganh(sinh_vien_list):
    print("\n--- Sap xep theo chuyen nganh ---")
    sinh_vien_list.sort(key=lambda sv: sv.chuyennganh)
    for sv in sinh_vien_list:
        print(sv)


def hien_thi_danh_sach(sinh_vien_list):
    print("\n--- Danh sach sinh vien ---")
    if sinh_vien_list:
        for sv in sinh_vien_list:
            print(sv)
    else:
        print("Danh sach sinh vien trong.")


def menu():
    sinh_vien_list = []
    while True:
        print("\n===== QUAN LY SINH VIEN =====")
        print("1. Them sinh vien")
        print("2. Cap nhat thong tin sinh vien theo ID")
        print("3. Xoa sinh vien theo ID")
        print("4. Tim kiem sinh vien qua ten")
        print("5. Sap xep danh sach sinh vien theo diem trung binh")
        print("6. Sap xep danh sach sinh vien theo ten chuyen nganh")
        print("7. Hien thi danh sach sinh vien")
        print("0. Thoat chuong trinh")

        lua_chon = input("Nhap lua chon cua ban: ")
        if lua_chon == '1':
            them_sinh_vien(sinh_vien_list)
        elif lua_chon == '2':
            cap_nhat_sinh_vien(sinh_vien_list)
        elif lua_chon == '3':
            xoa_sinh_vien(sinh_vien_list)
        elif lua_chon == '4':
            tim_kiem_sinh_vien(sinh_vien_list)
        elif lua_chon == '5':
            sap_xep_theo_diem(sinh_vien_list)
        elif lua_chon == '6':
            sap_xep_theo_chuyen_nganh(sinh_vien_list)
        elif lua_chon == '7':
            hien_thi_danh_sach(sinh_vien_list)
        elif lua_chon == '0':
            print("Ket thuc chuong trinh. Tam biet!")
            break
        else:
            print("Lua chon khong hop le. Vui long thu lai.")


if __name__ == '__main__':
    menu()
