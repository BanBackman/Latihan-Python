print(" Nama : RIZKY PRATAMA\n Kelas  : SISTEM INFORMASI 1.C\n Nim  : 701210181")

print('='*60)

y = int(input("Masukan jumlah bintang: "))
y = int(y)
 
if((y)):
    for rizky in range (0, y):
        for x in range (0,y):
            print("*" ,end="")
        for r in range(0,rizky):
            print("  ", end="")
        for b in range (0,y):
            print("*", end="")
        y-=1
        print()
