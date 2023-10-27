#2-Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

#Kullanıcıdan sayı al
sayi = int(input("Bir sayı giriniz: "))


toplam = 0
for i in range(1, sayi):
    if sayi % i == 0:
        toplam += i

#Sonuç

if toplam == sayi:
    print(f"{sayi} mükemmel bir sayıdır.")
else:
    print(f"{sayi} mükemmel bir sayı değildir.")