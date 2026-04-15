nilai = int(input("menghitung nilai:"))
absensi = int(input("menghitung absensi:"))

if nilai >70 and absensi >50:
    print("lulus")
elif (nilai <70 and absensi >70) or (nilai >70 and absensi <50):
    print("tidak lulus tapi bisa perbaikan nilai")
else:
    print("tidak lulus dan tidak bisa perbaikan nilai")