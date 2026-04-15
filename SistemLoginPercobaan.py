pw_benar = "JuwiJampangTengah"
percobaan = 0

while percobaan <3:
    pw_input = input("masukan password:")
    if pw_input == pw_benar:
        print("login berhasil!")
        break

    else:
        percobaan +=1
        print("password salah. Percobaan ke-", {percobaan})
    if percobaan ==3:
        print("akun terkunci")