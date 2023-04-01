sozluk = {"elma": "apple", "kitap": "book", "kalem": "pencil"}

# Sözlüklerin elemanlarına erişme
print(sozluk["elma"])
print(sozluk.get("elma"))
print(sozluk.get("siyah", "yok"))

# Sözlüklere eleman ekleme
sozluk["masa"] = "table"
sozluk["kırmızı"] = "red"
print(sozluk)

# Sözlüklerden eleman silme
del sozluk["masa"]
print(sozluk)

# SÖZLÜK METOTLARI
# keys()
print(sozluk.keys())

# values()
print(sozluk.values())

# items()
print(sozluk.items())

# İç içe sözlükler
ogrenciler = {
    "9/A": {"isim": "Eren", "soyad": "Özdal", "dogum_tarihi": 1986},
    "9/B": {"isim": "Ahmet", "soyad": "Yılmaz", "dogum_tarihi": 1998, "notlar": [80, 95]}
}
for sinif, ogrenci in ogrenciler.items():
    for key, value in ogrenci.items():
        print(f"Sınıf: {sinif}, {key}: {value}")

print(ogrenciler["9/B"]["notlar"])
