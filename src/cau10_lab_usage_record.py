from datetime import datetime

ma_phien = input("Nhap ma phien :")
ma_may = input("Nhap ma may :")
cong_suat_w = input("Nhap cong suat :")
thoi_gian = input("Nhap thoi gian :")
don_gia = input("Nhap don gia dien :")

cong_suat_w = float(cong_suat_w)
thoi_gian = int(thoi_gian)
don_gia = float(don_gia)

dien_nang_tieu_thu = cong_suat_w * thoi_gian / 60 / 1000
chi_phi = dien_nang_tieu_thu * don_gia

kiem_tra = thoi_gian > 60
thoi_diem = datetime.now()
print("Ma may la", ma_may)
print("Cong suat", cong_suat_w)
print("Thoi gian", thoi_gian)
print("Don gia dien", don_gia)
print("Kiem tra lon hon 60 dung hay khong:", kiem_tra)
print(f"Dien nang tieu thu {dien_nang_tieu_thu:.3f} kwh")
print(f"Chi phi {chi_phi:.2f} VND")
print(f"Ghi nhan luc : {thoi_diem.strftime("%Y-%m-%d %H:%M:%S")}")


print("Hoang Thien Lam_25174600212")
