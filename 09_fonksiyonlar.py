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


# FONKSİYONLARA PARAMETRE (ARGÜMAN) GÖNDERME
# Konumlarına göre parametre göndermek
def tam_ad_yaz(ad, soyad):
    print("Merhaba, benim adım " + ad + " " + soyad)


tam_ad_yaz("Eren", "Özdal")

# Anahtar kelimelere (değişken adı) göre parametre göndermek
tam_ad_yaz(soyad="Özdal", ad="Eren")


# Varsayılan parametreler
def tam_ad_yaz(ad, soyad=""):
    print("Merhaba, benim adım {} {}".format(ad, soyad))


tam_ad_yaz("Eren")
tam_ad_yaz("Eren", "Özdal")


# ESNEK SAYIDA PARAMETRE GÖNDERMEK
# *args parametresi
def toplama(*args):
    # *args: ()
    toplam = 0
    for sayi in args:
        toplam += sayi

    return toplam


print(toplama(4, 7, 10, 15))
print(toplama(5, 4))
print(toplama(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(toplama())


# **kwargs parametresi
def ogrenci_bilgileri(**kwargs):
    # **kwargs: {"ad": "Eren", "soyad": "Özdal", "yas": 37}
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")


ogrenci_bilgileri(ad="Eren", soyad="Özdal", yas=37, dersler=["Türkçe", "Matematik"])

# Lambda Fonksiyonları
liste = [1, 2, 3, 4, 5, 6, 7]
kareler = list(map(lambda x: x ** 2, liste))
print(kareler)

liste1 = [4, 6]
liste2 = [8, 12]
toplamlar = list(map(lambda x, y: x + y, liste1, liste2))
print(toplamlar)


# İç içe fonksiyonlar
def dort_islem(sayi1, sayi2, islem="toplama"):
    # toplama
    def toplama(x, y):
        return x + y

    # çıkarma
    def cikarma(x, y):
        return x - y

    # çarpma
    def carpma(x, y):
        return x * y

    # bölme
    def bolme(x, y):
        return x / y

    if islem == "toplama":
        return toplama(sayi1, sayi2)
    elif islem == "çıkarma":
        return cikarma(sayi1, sayi2)
    elif islem == "çarpma":
        return carpma(sayi1, sayi2)
    elif islem == "bölme":
        return bolme(sayi1, sayi2)
    else:
        return "Yanlış işlem seçtiniz"


print("Toplama:", dort_islem(2, 3))
print("Çıkarma:", dort_islem(8, 6, "çıkarma"))
print("Çarpma:", dort_islem(8, 6, "çarpma"))
print("Bölme:", dort_islem(64, 8, "bölme"))
print("Hata:", dort_islem(64, 8, "kare alma"))
