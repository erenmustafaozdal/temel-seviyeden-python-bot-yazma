from ogrenci import Ogrenci

ahmet = Ogrenci(isim="Ahmet", soyisim="Yılmaz", yil=2010)
ahmet.not_ekle(77)
ahmet.not_ekle(40)
print(ahmet.ad)
print(ahmet.soyad)
print(ahmet.dogum_yili)
print(ahmet.notlar)
print(ahmet.not_ortalama())

mehmet = Ogrenci("Mehmet", "Türker", 2008)
mehmet.not_ekle(85)
mehmet.not_ekle(60)
mehmet.not_ekle(90)
print(mehmet.ad)
print(mehmet.soyad)
print(mehmet.dogum_yili)
print(mehmet.notlar)
print(mehmet.not_ortalama())

zeynep = Ogrenci("Zeynep", "Ela", 2005)
print(zeynep.not_ortalama())
print(zeynep.tam_ad())

