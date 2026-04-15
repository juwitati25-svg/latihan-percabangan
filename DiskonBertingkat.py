diskon = int(input("masukan total belanja"))

if diskon >= 500000:
    print("mendapatkan diskon 20%")
elif diskon >= 300000:
    print("mendapatkan diskon 10")
elif diskon >= 100000:
    print("mendapatkan diskon 10%")
elif diskon < 100000:
    print("tidak ada diskon")