# İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacci_serisi = [1, 1]

while len(fibonacci_serisi) < 20:
    yeni_eleman = fibonacci_serisi[-1] + fibonacci_serisi[-2]
    fibonacci_serisi.append(yeni_eleman)

print(fibonacci_serisi)