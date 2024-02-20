# String İndeksleme ve Parçalama
isim = "Eren Mustafa Özdal"
print(isim[0])
print(isim[0:4])
print(isim[5::-1])
print(isim[::-1])

# String  karakterleri değiştirme ve Silme
metin = "Merhaba Dünya"
print(metin[:8] + "Türkiye")
# del metin[2]  -> string içindeki karakterler silinemez

# String birleştirme ve formatlama
kelime1 = "Merhaba"
kelime2 = "Dünya"
kelimeler = kelime1 + " " + kelime2
print(kelimeler)

isim = "Eren"
yas = 37
mesaj = "Benim adım {} ve yaşım {}".format(isim, yas)
print(mesaj)

mesaj = "Benim adım {1} ve yaşım {0}".format(yas, isim)
print(mesaj)

mesaj = "Benim adım {name} ve yaşım {age}".format(name=isim, age=yas)
print(mesaj)

mesaj = f"Benim adım {isim} ve yaşım {yas}"
print(mesaj)

# STRING METOTLARI
makale = "ramazan boyunca her gün saat 13.00'da canlı mukabele etkinliğimize davetlisiniz! İnstagram hesabımızdan canlı yayın yapacağımız bu etkinlikte, her gün farklı bir hafızımız Kur'an-ı Kerim tilaveti gerçekleştirecek. Siz de bizlerle birlikte bu mübarek ayda manevi bir yolculuğa çıkmak için takipte kalın..."

# capitalize()
print(makale.capitalize())

# upper()
print(makale.upper())

# lower()
print(makale.lower())

# title()
print(makale.title())

# strip()
metin = "        merhaba dünya        "
print(metin.strip())
print(metin.lstrip())
print(metin.rstrip())
print(makale.strip("ramazan"))

# replace()
print(makale.replace("ramazan", "şaban"))
print(makale.replace("bir", "iki", 1))  # ilk 1 eşleşmeyi değiştiriyor

# split()
print(makale.split())
print(makale.split(". "))

# join()
kelimeler = ["Merhaba", "benim", "adım", "Eren"]
cumle = ",".join(kelimeler)
print(cumle)
print(" ".join(kelimeler))

# count()
print(makale.count("a"))
print(makale.count("bir"))
print(makale.count("Instagram"))  # 0 çünkü; İnstagram yazılmış

# endswith()
print(makale.endswith("."))  # True

# startswith()
print(makale.startswith("ramazan"))  # True
print(makale.startswith("şaban"))  # False

# STRING KAÇIŞ DİZİLERİ
# \" : string içinde çift tırnak anlamına gelir
print("Eren \"Benim yaşım 37\" dedi")

# \' : string içinde tek tırnak anlamına gelir
print('Eren \'Benim yaşım 37\' dedi')

# \n : yeni satır karakter
print("Eren\nMustafa\nÖzdal")

# \t : sekme karakter
print("Eren\tMustafa\tÖzdal")

# \\ : ters bölü karakteri
print("Eren\\nazar")
