def printList():
    f = open('D:\Will\Lectures\Outside\AI Indonesia - Basic Python\AI.12\Tugas-2\DaftarKontak.txt', 'r')
    for i in f:
        print(f.read())
    f.close()

def addList():
    f = open('D:\Will\Lectures\Outside\AI Indonesia - Basic Python\AI.12\Tugas-2\DaftarKontak.txt', 'a')
    strNama = input("Masukkan nama kontak: ")
    strNum = input("Masukkan nomor kontak: ")
    f.write("Nama: " + strNama + "\n")
    f.write("Nomor: " + strNum + "\n\n")
    f.close()


