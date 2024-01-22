print(" Nama : RIZKY PRATAMA\n Kelas  : SISTEM INFORMASI 1.C\n Nim  : 701210181")

print("-"*50)
print("Pilih luas bidang yang akan di hitung : ")
print("-"*50)

bidang = ('Segitiga', 'Persegi', 'Lingkaran')

for b in range(3):
    print (b+1, bidang[b])
pilih = int(input("1/2/3 :"))
print("-"*50)

#Menghitung Luas Segitiga
if (pilih == 1):
    rumus = 0.5
    alas = int(input("Alas :"))
    tinggi = int(input("Tinggi :"))

    Luas_segitiga = rumus*alas*tinggi
    print("Luas segitiga yaitu = "+ str(Luas_segitiga))

elif (pilih == 2):
    sisi = int(input("sisi : "))
    rumus_2 = sisi*sisi

    print("Luas persegi adalah = "+ str(rumus_2))
    
elif (pilih == 3):
    phi = 3.14
    jari = float(input("Masukan panjang jari-jari lingkaran : "))
    Luas_lingkaran = phi*jari*jari

    print("Luas lingkaran = "+ str(Luas_lingkaran))

