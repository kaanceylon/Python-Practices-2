# Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.


# Kullanıcıdan sayıyı al
sayi = int(input("Bir sayı girin: "))

if sayi > 1:

    for i in range(1,sayi):
        if sayi % i == 0: # sayi döngüdeki i sayısına (herhangi bir sayi i) tam bölünüyorsa bu asal değildir.
           print(sayi, "asal bir sayı değildir.")
           break 
        else:
            print(sayi, "asal bir sayıdır.") 
    else:
        print(sayi, "Bir asal sayi değildir.")
    


