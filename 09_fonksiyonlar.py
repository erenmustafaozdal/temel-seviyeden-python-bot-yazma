"""
Fonksiyon tanımlarken Python içindeki özel ifadeleri
ve fonksiyon isimlerini kullanamayız.

Fonksiyon söz dizimi:

def fonsiyon_adi(parametre1, parametre2):
    # işlemler yapılır
    return deger
"""


# Toplama işlemi yapan bir fonksiyon yazalım
def topla(a, b):
    sonuc = a + b
    return sonuc


toplam = topla(7, 9)
print(toplam)
print(topla(4, 6))


# Faktoriyel hesaplayan bir fonksiyon yazalım
def faktoriyel(n):
    if n == 0:
        return 1

    return n * faktoriyel(n-1)


f = faktoriyel(5)
print(f)
