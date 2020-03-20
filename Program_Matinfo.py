#Enkripsi Caesar
def enkripc(masukan):
    for i in range(0, len(masukan)):
        id = (huruf.find(masukan[i].upper()) + 3) % 26
        output.append(huruf[id])
    print("".join(output))


def dekripc(masukan):
    for i in range(0, len(masukan)):
        id = (huruf.find(masukan[i].upper()) - 3) % 26
        output.append(huruf[id])
    print("".join(output))

#Enkripsi Vigenere
def enkripv(masukan, kunci):
    for i in range(0, len(masukan)):
        k = i % (len(kunci))
        id = (huruf.find(masukan[i].upper()) + huruf.find(kunci[k].upper()) )% 26
        output.append(huruf[id])
    print("".join(output))


def dekripv(masukan, kunci):
    for i in range(0, len(masukan)):
        k = i % (len(kunci))
        id = (huruf.find(masukan[i].upper()) - huruf.find(kunci[k].upper())) % 26
        output.append(huruf[id])
    print("".join(output))

huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    output = []
    print("Pilih Jenis Enkripsi \n 1. Caesar \n 2. Vigenere")
    pilihan = int(input("pilihan: "))

    if pilihan == 1:

        while True:
            print("Metode Caesar: \nApa yang ingin anda lakukan? \n 1. Enkripsi \n 2. Dekripsi")
            pilihan = int(input("pilihan: "))
            if pilihan == 1:
                masukan = input("Masukan teks: ")
                enkripc(masukan)
                break
            elif pilihan == 2:
                masukan = input("Masukan teks: ")
                dekripc(masukan)
                break
            else:
                print('Tidak ada pilihan itu')
                continue
    elif pilihan == 2:
        while True:
            print("Metode Vigenere: \nApa yang ingin anda lakukan? \n 1. Enkripsi \n 2. Dekripsi")
            pilihan = int(input("pilihan: "))

            if pilihan == 1:
                masukan = input("Masukan teks: ")
                kunci = input("Key: ")
                enkripv(masukan, kunci)
                break
            elif pilihan == 2:
                masukan = input("Masukan teks: ")
                kunci = input("Key: ")
                dekripv(masukan, kunci)
                break
            else:
                print('Tidak ada pilihan itu')
                continue
    else:
        print('Tidak ada pilihan itu')
        continue



    print("tekan y untuk mengulang: ")
    pilihan = input("pilihan: ")

    if pilihan == "y":
        continue
    else:
        break




