# Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

if (sayi1 > sayi2):
    kucukSayi = sayi2
else:
    kucukSayi = sayi1
for i in range(1, kucukSayi+1):
    if(sayi1% i == 0) and (sayi2 % i == 0): # iki sayı da i'ye tam bölünüyorsa ebob = i
        ebob = i

print("Ebob : ", ebob)
print("Ekok: ", (sayi1 * sayi2) // ebob) # iki sayının çarpımının ebob'a bölümü = ekok

