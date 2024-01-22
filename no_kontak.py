import csv

print("pilih salah satu")
print("----------------")
print("a. melihat list no kontak")
print("b. menambahkan no kontak")
in_pilih = input("pilihan a atau b: ")

if(in_pilih == "b"):
    in_nama = input("Masukan nama : ")
    in_no   = input("Masukan no telp: ")

    in_simpan = input("Tekan ketik y untuk menyimpan:")

    if(in_simpan == 'y'):
        with open('no_kontak.csv','a', newline='') as csv_file:
            # membuat objek writer
            writer = csv.writer(csv_file, delimiter=',')

            #menulis baris ke file csv
            writer.writerow([in_nama, in_no])
        print("Nomor tersimpan")

elif(in_pilih == "a"):
    kontak = []
    
    with open('no_kontak.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=",")
        for row in csv_reader:
            kontak.append(row)

    print("NAMA \t\t NOMOR")
    print("-"*34)
    for data in kontak:
        print(f'{data[0]} \t\t {data[1]}')
