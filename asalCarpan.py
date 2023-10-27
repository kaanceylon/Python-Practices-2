# Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 


# Kullanıcıdan sayıyı aldık
sayi = int(input("Bir sayı girin: "))

bolen = 2
for i in range(1,sayi):
    if(sayi % bolen == 0):
        print(bolen)
        sayi//=bolen
    else:
        bolen+=1