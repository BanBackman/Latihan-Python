import csv

print("Pilih salah satu")
print("----------------")
print("a. Melihat List Matkul")
print("b. Menambahkan Data")
in_pilih = input("pilihan a atau b: ")

if(in_pilih == "b"):
	in_kode = input("Massukkan Kode Matkul : ")
	in_nama   = input("Masukkan Nama Matkul: ")
	in_nilai = input("Masukkan Nilai : ")

	in_simpan = input("Tekan y untuk menyimpan: ")

	if(in_simpan   == 'y'):
		with open('nama_matkul.csv','a', newline='') as csv_file:
			#membuat objek writer
			writer = csv.writer(csv_file, delimiter=',')

			#menulis baris ke file CSV
			writer.writerow([in_kode, in_nama, in_nilai])
		print("Data Tersimpan")

elif(in_pilih == "a"):
	matkul = []

	with open('nama_matkul.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=",")
		for row in csv_reader:
			matkul.append(row)

	print("-"*60)
	print("KODE \t\t MATA KULIAH \t\t\t NILAI")
	print("-"*60)
	for data in matkul:
		print(f'{data[0]} \t\t {data[1]} \t\t {data[2]}')


