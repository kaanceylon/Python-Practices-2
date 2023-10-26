# Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# EBOB hesaplama fonksiyonu
def ebob_hesapla(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# EKOK hesaplama fonksiyonu
def ekok_hesapla(x, y):
    return (x * y) // ebob_hesapla(x, y)

# EBOB ve EKOK değerlerini hesapla
ebob = ebob_hesapla(sayi1, sayi2)
ekok = ekok_hesapla(sayi1, sayi2)

# Sonuç
print(f"{sayi1} ve {sayi2} için EBOB: {ebob}")
print(f"{sayi1} ve {sayi2} için EKOK: {ekok}")