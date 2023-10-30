krediler = ["Hızlı Kredi", "Maaşını HalkBank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]

#ailas
for kredi in krediler:
    print(kredi) # kredi yerine istediğimiz her isim olur. 

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3,10): # 3 dahil 10 dahil değil.
    print(i)
for i in range(0,11, 2): # 0 2 4 6 8 10 çıktımız
    print(i)