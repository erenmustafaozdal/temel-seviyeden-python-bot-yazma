import random

kelimeler = ["ofsayt", "penaltı", "serbest vuruş", "korner", "kaleci", "savunma", "orta saha", "forvet", "kırmızı kart", "sarı kart", "hakem",
             "çalım", "şut", "pas", "çalım atmak", "kafa vuruşu", "kale direği", "faul", "çapraz koşu", "korner vuruşu", "penaltı atışı", "futbol sahası"]

# Rastgele bir kelime seç
hedef_kelime = random.choice(kelimeler)
dogru_tahmin = False
tahmin_hakki = 6  # Toplam 6 tahmin hakkı
bulunanlar = []
print("Kelime Tahmin Oyununa Hoş Geldiniz!")

while tahmin_hakki > 0:
    # Kalan tahmin hakkını ve hedef kelimeyi göster
    print(f"Kalan Canlar: {'❤️ ' * tahmin_hakki}")

    # Kelime gösterim
    gosterim = []
    for karakter in hedef_kelime:
        if karakter == " " or karakter in bulunanlar:
            gosterim.append(karakter)
        else:
            gosterim.append("_")
    hedef_kelime_gosterimi = " ".join(gosterim)
    print("Hedef Kelime: " + hedef_kelime_gosterimi)

    # Kullanıcıdan bir harf tahmini al
    tahmin = input("Bir harf tahmini yapın: ").lower()

    if len(tahmin) != 1 or not tahmin.isalpha():
        print("Geçersiz giriş. Lütfen bir harf girin.")
        continue

    # Harfin doğru olup olmadığını kontrol et
    if tahmin in hedef_kelime:
        print("Doğru tahmin! 🎉")
        bulunanlar.append(tahmin)
    else:
        print("Yanlış tahmin. 😔")
        tahmin_hakki -= 1

    # Tüm harfleri doğru tahmin ettiyse oyunu kazandı
    if set(harf for harf in hedef_kelime) == set(harf for harf in hedef_kelime if harf in bulunanlar):
        dogru_tahmin = True
        break

# Oyun sonucunu göster
if dogru_tahmin:
    print(
        f"Tebrikler! Hedef kelimeyi doğru tahmin ettiniz. Kelime: {hedef_kelime}")
else:
    print(f"Üzgünüm, canlarınız bitti. Hedef kelime: {hedef_kelime}")
print(f"Oyun bitti. Puanınız: {tahmin_hakki} ⭐")
