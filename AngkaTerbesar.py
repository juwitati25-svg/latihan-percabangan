angka1 = int(input("masukan angka1:"))
angka2 = int(input("masukan angka2:"))
angka3 = int(input("masukan angka3:"))

if angka1 > angka2 and angka1 > angka3:
    print("angka terbesar adalah:", angka1)
elif angka2 > angka1 and angka2 > angka3:
    print("angka terbesar adalah:", angka2)
else:
    print("angka terbesar adalah:", angka3)