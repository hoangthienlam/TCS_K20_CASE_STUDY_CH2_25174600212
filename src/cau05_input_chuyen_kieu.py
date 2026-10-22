ma_may = input("Ma may la :",)
cong_suat_W = input("Cong suat la :")
so_phut = input("So phut su dung la:")
don_gia_dien_Kwh = input("Don gia la :")

print(type(ma_may))
print(type(cong_suat_W))
print(type(so_phut))
print(type(don_gia_dien_Kwh))

cong_suat_W = float(cong_suat_W)
so_phut = int(so_phut)
don_gia_dien_Kwh = float(don_gia_dien_Kwh)

dien_nang_tieu_thu = cong_suat_W *so_phut / 60 / 100
chi_phi = don_gia_dien_Kwh * dien_nang_tieu_thu
print("dien_nang_tieu_thu", dien_nang_tieu_thu)
print("chi_phi", chi_phi)