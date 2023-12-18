import random

can_sayisi = 10  # Başlangıçta 10 can
puan = 0

print("Sayı Tahmin Oyununa Hoş Geldiniz!")
print("1 ile 100 arasında bir sayı seçildi.")

# Bilgisayar rastgele bir sayı seçsin
hedef_sayi = random.randint(1, 100)

while can_sayisi > 0:
    # Oyuncunun can sayısını ve puanını yazdır
    print(f"Canlar: {'❤️ ' * can_sayisi}")

    # Oyuncudan bir tahmin iste
    tahmin = int(input("Tahmininizi girin: "))

    # Tahminin doğruluğunu kontrol et
    if tahmin < hedef_sayi:
        print("Daha büyük bir sayı girin.")
    elif tahmin > hedef_sayi:
        print("Daha küçük bir sayı girin.")
    else:
        print(f"Tebrikler! Doğru bildiniz. Hedef sayı: {hedef_sayi}")
        puan += 10 * can_sayisi
        break

    can_sayisi -= 1
    if can_sayisi == 0:
        print(f"Üzgünüm, canlarınız bitti. Doğru cevap {hedef_sayi} idi.")

print(f"Oyun bitti. Puanınız: {puan} ⭐")
