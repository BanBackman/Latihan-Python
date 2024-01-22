import csv 

print(" Nama : RIZKY PRATAMA\n Kelas  : SISTEM INFORMASI 1.C\n Nim  : 701210181")

def cek_barang(Storage, nama):

    for i in range(len(Storage)):
        if(Storage[i]['nama'] == nama):
            print(nama)
            return True
    return False

def print_data(Storage):
    print('===================================================================================')
    print('Data barang')
    print('===================================================================================')

    for i in range(len(Storage)):
        print('Nama: ',Storage[i]['nama'])
        print('harga: ',Storage[i]['harga'])
        print()

def in_Barang(Storage, nama, harga):

    if(cek_barang(Storage, nama)):
        print('Data sudah tersedia')
    else:
        _id = len(Storage)
        data_barang = {'id':_id, 'nama':nama, 'harga':harga,}
        Storage.append(data_barang)
        lihat_data_barang = input('Lihat Data Barang (y/n):')
        if(lihat_data_barang == 'y'):
            print_data(Storage)
        else:
            print('Data Tersimpan')

def cek_namaBarang(Storage, _id):

    for i in range(len(Storage)):
        if(Storage[i]['id'] == int(_id)):
            return Storage[i]
    else:
        return None

Storage_ = [
{
    'id':0,
    'nama':'Samsung A10',
    'harga':2300000,
},
{
    'id':1,
    'nama':'Redmi Note 10',
    'harga':3700000,
},
{
    'id':2,
    'nama':'OPPO A95',
    'harga':2700000,
},
]

Transaksi_ =[]

ulang = True
while(ulang):
    print('===============================================================================')
    print('Menu Pilihan')
    print('===============================================================================')
    print('1. Input Barang')
    print('2. Transaksi')
    print('3. Laporan')

    pilihan_in = input('Masukkan Pilihan:')

    if(pilihan_in =='1'):
        print('/n===================================================================================')
        print('Masukkan Data Barang')
        print('=====================================================================================')
        in_nama = input('Nama Barang:')
        in_harga = input('Harga Barang:')

        in_Barang(Storage_, in_nama, in_harga)

    elif(pilihan_in == '2'):
        print('/n===================================================================================')
        print('List kode Barang')
        print('=====================================================================================')

        for i in range(len(Storage_)):
            print(Storage_[i]['id'],'-',Storage_[i]['nama'])

        print('/n===================================================================================')
        print('Transaksi')
        print('=====================================================================================')
        ulg_transaksi = True
        list_transaksi = []

        while(ulg_transaksi):
            input_id = input('Masukkan kode barang:')

            if(cek_namaBarang(Storage_,input_id)!= None):
                barang = cek_namaBarang(Storage_,input_id)
                print(barang['nama'],' ',end='')
                input_jumlah = input('jumlah:')
                in_transaksi = {'id':input_id,'nama':barang['nama'],'harga':barang['harga'], 'jumlah':input_jumlah}
                list_transaksi.append(in_transaksi)
            else:
                print('Barang tidak tersedia')

            in_kode_lg = input('Tambah barang (y/t)?')
            if(in_kode_lg == 'y'):
               ulg_transaksi = True
            else:
                ulg_transaksi = False
        
        total_harga = 0
        print('/n===================================================================================')
        print('Nama /t Harga /t/t Jumlah /t/t Total')
        print('=====================================================================================')
        for i in range(len(list_transaksi)):

            jumlah = float(list_transaksi[i]['harga'])*int(list_transaksi[i]['jumlah'])
            print(list_transaksi[i]['nama'],'/t/t',list_transaksi[i]['harga'],'/t/t',list_transaksi[i]['jumlah'],'/t/t',list_transaksi[i], jumlah)

            total_harga=total_harga+jumlah
        print('/n===================================================================================')
        print('Total Bayar:', total_harga)
        print('=====================================================================================')

        transaksi_item = {'_id':len(Transaksi_),'Transaksi':list_transaksi,'Total':total_harga}
        Transaksi_.append(transaksi_item)

    elif(pilihan_in == '3'):
        total_transaksi_sesi = 0
        print('/n===================================================================================')
        print('ID/t/tTotal')
        for i in range(len(list_transaksi)):
            print(Transaksi_[i]['_id'],Transaksi_[i]['Total'])
            total_transaksi_sesi = total_transaksi_sesi+Transaksi_[i]['Total']
        print('===================================================================================')
        print('Total Transaksi Sesi ini:',total_transaksi_sesi) 