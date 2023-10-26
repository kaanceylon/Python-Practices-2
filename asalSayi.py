# Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.


# Kullanıcıdan sayıyı al
sayi = int(input("Bir sayı girin: "))

# Asal sayı kontrol fonksiyonu
def asal_sayi_kontrolu(sayi):
    if sayi <= 1:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

# Asal sayı kontrol fonksiyonunu kullanarak sonucu ekrana yazdır
if asal_sayi_kontrolu(sayi):
    print(sayi, "asal bir sayıdır.")
else:
    print(sayi, "asal bir sayı değildir.")