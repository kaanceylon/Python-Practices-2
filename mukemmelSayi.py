# Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

# Kullanıcıdan sayıyı al
sayi = int(input("Bir sayı girin: "))

# Mükemmel sayıyı kontrol etmek için bir fonksiyon tanımla
def mukemmel_sayi_kontrolu(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

# Kullanıcının girdiği sayının mükemmel olup olmadığını kontrol et
if mukemmel_sayi_kontrolu(sayi):
    print(sayi, "mükemmel bir sayıdır.")
else:
    print(sayi, "mükemmel bir sayı değildir.")