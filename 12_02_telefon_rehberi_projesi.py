# Telefon rehberi için boş bir sözlük oluşturuluyor.
rehber = {}

# Rehberde bir kişi eklemek için bir fonksiyon tanımlayalım.
def kisi_ekle(ad, numara):
    """
    Rehbere yeni bir kişi ekler.

    :param ad: Kişinin adı.
    :param numara: Kişinin telefon numarası.
    """
    if ad in rehber:
        print(f"{ad} zaten rehberde var.")
    else:
        rehber[ad] = numara
        print(f"{ad} rehbere eklendi.")

# Rehberden bir kişiyi silmek için bir fonksiyon tanımlayalım.
def kisi_sil(ad):
    """
    Rehberden bir kişiyi siler.

    :param ad: Silinecek kişinin adı.
    """
    if ad in rehber:
        del rehber[ad]
        print(f"{ad} rehberden silindi.")
    else:
        print(f"{ad} rehberde bulunamadı.")

# Rehberdeki bir kişinin numarasını güncellemek için bir fonksiyon tanımlayalım.
def numara_guncelle(ad, yeni_numara):
    """
    Rehberdeki bir kişinin numarasını günceller.

    :param ad: Numarası güncellenecek kişinin adı.
    :param yeni_numara: Yeni telefon numarası.
    """
    if ad in rehber:
        rehber[ad] = yeni_numara
        print(f"{ad}'nin numarası güncellendi.")
    else:
        print(f"{ad} rehberde bulunamadı.")

# Rehberdeki tüm kişileri listelemek için bir fonksiyon tanımlayalım.
def rehberi_listele():
    """
    Rehberdeki tüm kişileri listeler.
    """
    if rehber:
        print("Telefon Rehberi:")
        for ad, numara in rehber.items():
            print(f"{ad}: {numara}")
    else:
        print("Rehber boş.")

# Ana döngü
while True:
    print("\nTelefon Rehberi Uygulaması")
    print("1. Kişi Ekle")
    print("2. Kişi Sil")
    print("3. Numara Güncelle")
    print("4. Rehberi Listele")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        ad = input("Kişinin adını girin: ")
        numara = input("Kişinin numarasını girin: ")
        kisi_ekle(ad, numara)
    elif secim == "2":
        ad = input("Silmek istediğiniz kişinin adını girin: ")
        kisi_sil(ad)
    elif secim == "3":
        ad = input("Numarasını güncellemek istediğiniz kişinin adını girin: ")
        yeni_numara = input("Yeni numarayı girin: ")
        numara_guncelle(ad, yeni_numara)
    elif secim == "4":
        rehberi_listele()
    elif secim == "5":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem! Lütfen tekrar deneyin.")
