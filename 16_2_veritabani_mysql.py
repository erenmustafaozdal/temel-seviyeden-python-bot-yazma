import mysql.connector
from ayarlar import *

# MySQL veritabanına bağlanalım
baglanti = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

# Veritabanı işlemleri için imleç nesnesi oluşturalım
imlec = baglanti.cursor()

# Veritabanı tablosu oluşturalım
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad CHAR(50), soyad CHAR(25), dogum_tarihi SMALLINT)")

# Veritabanına veri ekleyelim
sql = "INSERT INTO ogrenciler (ad, soyad, dogum_tarihi) VALUES (%s, %s, %s)"
params = ("Mehmet", "Öner", 2014)
imlec.execute(sql, params)

# İşlemleri kaydedelim
baglanti.commit()

# Bağlantıyı kapatalım
baglanti.close()
