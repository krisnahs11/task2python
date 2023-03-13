gaji = 10000000
berkeluarga = True
punya_rumah = True

if gaji > 3000000 :
    print("gaji sudah diatas UMR")
    if berkeluarga:
        print("wajib ikut asuransi dan menabung untuk pensiun")
    else:
        print("tidak perlu ikut berasuransi")
    if punya_rumah:
        print("wajib bayar pajak rumah")
    else:
        print("tidak wajib bayar pajak rumah")
else:
    print("gaji belum UMR")