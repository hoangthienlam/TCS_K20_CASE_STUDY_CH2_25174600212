ma_phien = "LABO26"
ma_may = "PC12"
cong_suat_W = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_tieu_thu = cong_suat_W * so_phut / 60 / 1000
chi_phi = don_gia_kwh * dien_nang_tieu_thu

print("Ma phien :", ma_phien)
print("Ma may:", ma_may)
print("Dien nang :", dien_nang_tieu_thu)
print("Chi phi", chi_phi)
