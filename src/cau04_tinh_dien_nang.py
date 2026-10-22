cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(dien_nang_kwh) # in ra 0.375
print(chi_phi) # in ra 1125.0
print("Dien nang tieu thu:", dien_nang_kwh, type(dien_nang_kwh)) # float
print("Chi phi dien:", chi_phi, type(chi_phi)) # float

so_phut = 60
dien_nang_kwh_2 = cong_suat_w *so_phut / 60 / 1000
chi_phi_2 = dien_nang_kwh *don_gia_kwh
print(dien_nang_kwh_2)
print(chi_phi_2)
print(dien_nang_kwh > dien_nang_kwh_2)
print(dien_nang_kwh < dien_nang_kwh_2)
print(chi_phi > chi_phi_2)
print(chi_phi < chi_phi_2)