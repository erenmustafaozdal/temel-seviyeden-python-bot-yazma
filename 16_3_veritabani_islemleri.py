import sqlite3

# Veritabanı oluşturma
baglanti = sqlite3.connect("okul.db")

# İmleç nesnesi oluşturalım
imlec = baglanti.cursor()

# Tablo oluşturalım
imlec.execute("""CREATE TABLE IF NOT EXISTS ogrenciler (
    id INTEGER PRIMARY KEY,
    ad TEXT,
    soyad TEXT,
    sinif INTEGER,
    sube TEXT,
    dogum_tarihi TEXT,
    notlar TEXT
)""")

while True:
    cevap = input("""Lütfen yapılacak işlemi seçin:
    1. Öğrenci ekle
    2. Öğrenci düzenleme
    3. Öğrencileri Listele
    4. Öğrenci sil
    0. Çıkış 
    """)

    # Çıkış işlemi
    if cevap == "0":
        break

    # Öğrenci ekleme işlemi
    if cevap == "1":
        ad = input("Öğrenci adı: ")
        soyad = input("Öğrenci soyadı: ")
        sinif = int(input("Öğrenci sınıf: "))
        sube = input("Öğrenci şubesi: ")
        dogum = input("Öğrenci doğum tarihi (gg/aa/yyyy): ")
        notlar = input("Öğrenci notları (virgülle ayrılmış): ")

        imlec.execute(f"INSERT INTO ogrenciler (ad, soyad, sinif, sube, dogum_tarihi, notlar) VALUES ('{ad}', '{soyad}', {sinif}, '{sube}', '{dogum}', '{notlar}')")
        baglanti.commit()

    # Öğrenci düzenleme
    elif cevap == "2":
        ad = input("Düzenlenecek öğrencinin adı: ")
        notlar = input("Öğrenci notları (virgülle ayrılmış): ")

        imlec.execute(f"UPDATE ogrenciler SET notlar = '{notlar}' WHERE ad = '{ad}'")
        baglanti.commit()

    # Öğrencileri listeleme
    elif cevap == "3":
        imlec.execute("SELECT * FROM ogrenciler")

        ogrenciler = imlec.fetchall()
        for ogrenci in ogrenciler:
            print(ogrenci)

    # Öğrenci sil
    else:
        ad = input("Silinecek öğrencinin adı: ")
        imlec.execute(f"DELETE FROM ogrenciler WHERE ad = '{ad}'")
        baglanti.commit()


# İşlemleri kaydedelim
baglanti.commit()

# Bağlantıyı kapatalım
baglanti.close()

