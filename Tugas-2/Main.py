import contModule

def menu():
    print("1. Daftar Kontak")
    print("2. Tambahkan Kontak")
    print("3. Keluar")

menu()

option = int(input("Pilih menu: "))

while option != 0:
    if option == 1:
        contModule.printList()
    elif option == 2:
        contModule.addList()
        print("\nKontak berhasil ditambahkan!")
    elif option == 3:
        print("Terima kasih sudah menggunakan program ini!")
        exit()
    else:
        print("Menu tidak tersedia.\n")

    print()
    menu()
    option = int(input("Pilih menu: "))