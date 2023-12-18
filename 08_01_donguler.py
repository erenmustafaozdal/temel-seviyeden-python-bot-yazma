"""
for: liste (list), sözlük (dict), demet (tuple) gibi veri tiplerinin
    içindeki elemanları döngü içinde kullanmaya yarar.
while: belirli bir koşul sağlandığı sürece devam eden döngülerdir.
"""

# For Döngüsü
# Liste elemanlarına ulaşalım
liste = [1, 2, "elma", "çilek"]
for eleman in liste:
    print(eleman)

# Sayıları toplayalım
liste2 = [1, 5, 9, 16, 21, 3]
toplam = 0
for eleman in liste2:
    # toplam = toplam + eleman  -> uzun versiyon
    toplam += eleman  # kısa versiyonu

print(toplam)

# Liste elemanlarının değerlerini değiştirelim
liste3 = [1, 2, 3, 4, 5]
for i, eleman in enumerate(liste3):
    liste3[i] = eleman * eleman  # eleman ** 2

print(liste3)

# Liste elemanları içinde filtreleme yapalım
liste4 = [100, 101, 102, 103, 104, 105]
filtreli_liste = []
for eleman in liste4:
    if eleman % 2 == 0:
        filtreli_liste.append(eleman)

print(filtreli_liste)

# Çok boyutlu listeler içinde dolaşalım
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for eleman in matris:
    for ic_eleman in eleman:
        print(ic_eleman)

    print("---")

# While Döngüsü
# Sayı tahmin oyunu
import random

sayi = random.randint(1, 10)
tahmin = 10  # int(input("Sayıyı tahmin edin: "))

while False: # tahmin != sayi:
    # tahmin sayıdan büyükse
    if tahmin > sayi:
        print("Daha küçük bir sayı tahmin edin.")
    # tahmin sayıdan küçükse
    else:
        print("Daha büyük bir sayı tahmin edin.")

    tahmin = int(input("Tekrar tahmin edin: "))

print(f"Tebrikler! {sayi} sayısını doğru tahmin ettiniz.")

# Faktöriyel haesaplayalım
# 5! = 5 * 4 * 3 * 2 * 1
sayi = 5  # int(input("Faktöriyel hesabı için sayı yazın: "))
baslangic = sayi
faktoriyel = 1

while sayi > 0:
    faktoriyel *= sayi
    sayi -= 1

print(f"{baslangic} sayısının faktöriyeli {faktoriyel} sayısıdır.")

# İç içe döngüler
for i in range(5, 10):
    print(f"Dıştaki döngünün elemanı: {i}")
    j = 1
    while j < i:
        print(f"İçteki döngünün elemanı: {j}")
        j += 1

    print("-"*10)

# List Comprehension
# Uzun yol: Normal döngü
liste = []
for i in range(5):
    liste.append(i)

print(liste)

# Kısa yol: list comprehension
liste = [i for i in range(5)]
print(liste)

# Yukarıdaki karesini alma örneğini kısaca yapalım
liste3 = [i * i for i in liste3]
print(liste3)

# Liste elemanları içinde filtreleme yapalım kısaca yapalım
f_liste = [i for i in liste4 if i % 2 == 0]
print(f_liste)
