# Sorular ve cevaplar (Örnek sorular, gerçek bilgiler içermeyebilir)
sorular = [
    ("Türkiye, 2002 Dünya Kupası'nda yarı finale çıktı. (d/y)", "d"),
    ("Galatasaray, 2000 yılında UEFA Kupası'nı kazandı. (d/y)", "d"),
    ("Fenerbahçe, 1996 yılında Süper Lig'de şampiyon olmuştur. (d/y)", "y"),
    ("Beşiktaş, 2003 yılında UEFA Şampiyonlar Ligi'nde çeyrek final oynadı. (d/y)", "y"),
    # Aşağıdaki sorular örnek amaçlıdır ve gerçek bilgileri yansıtmayabilir
    ("2001 yılında Trabzonspor, Türkiye Kupası'nı kazandı. (d/y)", "d"),
    ("1993 yılında Bursaspor, Süper Lig'i ilk 4 içinde bitirdi. (d/y)", "y"),
    ("2004 yılında Türkiye, Avrupa Şampiyonası'na katıldı. (d/y)", "y"),
    ("1990 yılında Aykut Kocaman, gol kralı oldu. (d/y)", "d"),
    ("2005 yılında Ankaragücü, UEFA Kupası'na katıldı. (d/y)", "y"),
    ("1999 yılında Galatasaray, Süper Lig'de şampiyon oldu. (d/y)", "d"),
    ("2000 yılında Beşiktaş, Türkiye Kupası'nı kazandı. (d/y)", "y"),
    ("1995 yılında Fenerbahçe, UEFA Kupası çeyrek finali oynadı. (d/y)", "d"),
    ("2002 yılında Gaziantepspor, ligi ilk 5 içinde tamamladı. (d/y)", "d"),
    ("2001 yılında Rıdvan Dilmen futbolu bıraktı. (d/y)", "y"),
    ("2003 yılında Trabzonspor, ligi ikinci sırada tamamladı. (d/y)", "y"),
    ("1992 yılında Samsunspor, ligi ilk 3 içinde bitirdi. (d/y)", "y"),
    ("1998 yılında Hakan Şükür, Galatasaray'da en fazla gol atan oyuncu oldu. (d/y)", "d"),
    ("2000 yılında UEFA Kupası finalinde Galatasaray, Arsenal'ı yendi. (d/y)", "d"),
    ("1997 yılında Beşiktaş, Süper Lig'de şampiyon oldu. (d/y)", "d"),
    ("1994 yılında Türkiye, Dünya Kupası'na katıldı. (d/y)", "y")
]


can_sayisi = 3  # Başlangıç can sayısı
puan = 0  # Başlangıç puanı

# Döngü ile Soruları Sorma ve Cevapları Kontrol Etme

for soru, dogru_cevap in sorular:
    # Kalan canları ve mevcut puanı göster
    print(f"Kalan Can: {'❤️ ' * can_sayisi}")
    print(f"Mevcut Puan: {'⭐️' * puan}")

    cevap = input(soru + " Cevabınız: ").lower()

    if cevap == dogru_cevap:
        puan += 1  # Doğru cevap için puan artırma
        print("Doğru! +1 puan.")
    else:
        can_sayisi -= 1  # Yanlış cevap için can azaltma
        print("Yanlış! Bir can kaybettiniz.")

    if can_sayisi == 0:
        break  # Canlar bittiğinde oyunu bitir

# Oyunun Sonu

print(f"Oyun Bitti. Toplam Puanınız: {'⭐️' * puan}")

# Not: Bu kod doğrudan çalıştırıldığında 'input' fonksiyonu nedeniyle hata verecektir.
# Gerçek bir Python ortamında çalıştırılmalıdır.
