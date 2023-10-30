from luas.menu import menu
from luas.persegi import persegi
from luas.lingkaran import lingkaran
from luas.segitiga import segitiga

menu()
while 1:
    pilih = input("Masukkan pilihan : ")
    if pilih == "1":
        persegi()
    elif pilih == "2":
        lingkaran()
    elif pilih == "3":
        segitiga()
    else:
        print("Maaf, pilihan yang anda masukkan tidak terdaftar")
print("Coba lagi [Y/N]? ")
coba = input().upper()
if coba == "Y":
    menu()
else:
    print("\n yasudah kalo begitu")