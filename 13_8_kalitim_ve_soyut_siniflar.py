from abc import ABC, abstractmethod
# ABC (Abstract Base Class) kullanılarak soyut sınıf tanımlanır


class Sanatci(ABC):
    def __init__(self, ad, soyad, ulke):
        self.ad = ad
        self.soyad = soyad
        self.ulke = ulke


class SanatEseri(ABC):
    def __init__(self, ad, sanatci):
        self.ad = ad
        self.sanatci = sanatci
        self.sergide_mi = False

    @abstractmethod
    def sergiye_koy(self):
        pass

    @abstractmethod
    def depoya_koy(self):
        pass


class Tablo(SanatEseri):
    def __init__(self, ad, sanatci, teknik):
        super().__init__(ad, sanatci)
        self.teknik = teknik

    def sergiye_koy(self):
        if not self.sergide_mi:
            print(f"{self.ad} adlı tablo sergiye konuldu.")
            self.sergide_mi = True
        else:
            print(f"{self.ad} adlı tablo zaten sergide.")

    def depoya_koy(self):
        if self.sergide_mi:
            print(f"{self.ad} adlı tablo depoya kaldırıldı.")
            self.sergide_mi = False
        else:
            print(f"{self.ad} adlı tablo zaten depoda.")

    def __str__(self):
        return f"{self.ad} - {self.sanatci.ad} {self.sanatci.soyad} ({self.teknik})"


class Heykel(SanatEseri):
    def __init__(self, ad, sanatci, malzeme):
        super().__init__(ad, sanatci)
        self.malzeme = malzeme

    def sergiye_koy(self):
        if not self.sergide_mi:
            print(f"{self.ad} adlı heykel sergiye konuldu.")
            self.sergide_mi = True
        else:
            print(f"{self.ad} adlı heykel zaten sergide.")

    def depoya_koy(self):
        if self.sergide_mi:
            print(f"{self.ad} adlı heykel depoya kaldırıldı.")
            self.sergide_mi = False
        else:
            print(f"{self.ad} adlı heykel zaten depoda.")

    def __str__(self):
        return f"{self.ad} - {self.sanatci.ad} {self.sanatci.soyad} ({self.malzeme})"


class Galeri:
    def __init__(self, ad):
        self.ad = ad
        self.sanatcilar = []
        self.sanat_eserleri = []

    def sanatci_ekle(self, sanatci):
        self.sanatcilar.append(sanatci)
        print(f"{sanatci.ad} {sanatci.soyad} galeriye eklendi.")

    def eser_ekle(self, eser):
        self.sanat_eserleri.append(eser)
        print(f"{eser.ad} galeriye eklendi.")

    def sergiyi_goster(self):
        print(f"\nGalerideki Sanat Eserleri:")
        for eser in self.sanat_eserleri:
            if eser.sergide_mi:
                print(eser)
        print("\n")


# Örnek kullanım
picasso = Sanatci("Pablo", "Picasso", "İspanya")
monet = Sanatci("Claude", "Monet", "Fransa")

galeri = Galeri("Modern Sanat Galerisi")

galeri.sanatci_ekle(picasso)
galeri.sanatci_ekle(monet)

guernica = Tablo("Guernica", picasso, "Yağlı boya")
water_lilies = Tablo("Water Lilies", monet, "Yağlı boya")

galeri.eser_ekle(guernica)
galeri.eser_ekle(water_lilies)

guernica.sergiye_koy()
water_lilies.sergiye_koy()

galeri.sergiyi_goster()

guernica.depoya_koy()

galeri.sergiyi_goster()
