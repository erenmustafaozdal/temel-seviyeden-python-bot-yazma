import sqlite3

# Veritabanına bağlanalım
baglanti = sqlite3.connect("ornek.db")

# Veritabanında işlem yapılmasını sağlayan imleç nesnesi
imlec = baglanti.cursor()

# Veritabanı tablosu oluşturalım
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad text, soyad text, dogum_tarihi integer)")

# Veritabanına veri ekleyelim
imlec.execute("INSERT INTO ogrenciler VALUES ('Ahmet', 'Yılmaz', '2008')")

# İşlemleri kaydedelim
baglanti.commit()

# Bağlantıyı kapatalım
baglanti.close()
