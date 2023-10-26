# Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 


# Kullanıcıdan sayıyı aldık
sayi = int(input("Bir sayı girin: "))

# Asal çarpanları bulan fonksiyon
def asal_carpanlari_bul(sayi):
    asal_carpanlar = []
    i = 2
    while i <= sayi:
        if sayi % i == 0:
            asal_carpanlar.append(i)
            sayi //= i
        else:
            i += 1
    return asal_carpanlar

# Asal çarpanları bulan fonksiyonu çağır ve sonucu ekrana yazdır

asal_carpanlar = asal_carpanlari_bul(sayi)
print(f"{sayi} sayısının asal çarpanları: {asal_carpanlar}")