total_belanja = int(input("masukan total belanja:"))

if total_belanja >= 100000:
    print("mendapatkan diskon 10%")
    diskon = total_belanja * 0.1
else:
    print("tidak mendapatkan diskon")
    diskon = 0

total_bayar = total_belanja - diskon
print(f"total belanja juwi: Rp.{total_belanja:,}, diskon yang didapat: Rp.{diskon:,}, total yang harus dibayar: Rp.{total_bayar:,}")
