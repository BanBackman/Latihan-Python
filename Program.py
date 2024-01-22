print(" Nama : RIZKY PRATAMA\n Kelas  : SISTEM INFORMASI 1.C\n Nim  : 701210181")

print('='*60)

# POS Sederhana

def cek_barang(Storage, nama):

    for i in range(len(Storage)):
        if(Storage[i]['nama'] == nama):
            print(nama)
            return True
    return False

def print_data(Storage):
    print("\n===================================================================")
    print("Data Barang")
    print("=====================================================================")

    for i in range(len(Storage)):
        print("Nama: ",Storage[i]['nama'])
        print("Harga: ",Storage[i]['harga'])
        print()

def in_barang(Storage, nama, harga):

    # jika nama barang sudah tersedia di data
    if(cek_barang(Storage, nama)):
        print("Data sudah tersedia")
    else:
        # id di dapat dari jumlah data dalam storage
        _id = len(Storage)
        data_barang = {
                        "id":_id,
                        "nama":nama,
                        "harga":harga,
                   }
    Storage.append(data_barang)
    lihat_data_barang = input("Lihat Data Barang (y/n):")
    if(lihat_data_barang == "y"):
        print_data(Storage)
    else:
        print("Data Tersimpan")

def cek_namaBarang(Storage, _id):

    for i in range(len(Storage)):
        if(Storage[i]["id"] == int(_id)):
            return Storage[i]
    else: 
        return None 

Storage_= [
           {
               "id":0,
               "nama": "samsung A10",
               "harga":2300000,
           },
           {
               "id":1,
               "nama": "redmi note 10"
               "harga" : 3700000,
           },
           {
               "id":2,
               "nama": "OPPO"
               "harga":2700000,
           },        
]

