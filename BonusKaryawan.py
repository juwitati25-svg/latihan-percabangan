masa_kerja = int(input("masukan masa kerja karyawan(dalam tahun):"))
performa = input("masukan performa karyawan(baik/buruk):")

if masa_kerja>=5 and performa == "baik":
    print("mendapatkan bonus besar")
elif masa_kerja>=5 and performa == "buruk":
    print("mendapatkan bonus kecil")
else:
    print("tidak mendapatkan bonus")