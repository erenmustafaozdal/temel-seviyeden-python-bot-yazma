liste = [1, 2, True, "Eren", (1,2,3), {"a": 12, "b": 7}]

# Listenin elemanlarına erişme
print(liste[0])
print(liste[-1])

# Listenin elemanlarını değiştirme
liste[2] = "elma"
print(liste)

# LİSTE METOTLARI
# append()
meyveler = ["elma", "armut", "çilek"]
meyveler.append("erik")
print(meyveler)

# insert()
meyveler.insert(2, "karpuz")
print(meyveler)

# remove()
meyveler.append("erik")
print(meyveler)
meyveler.remove("erik")
print(meyveler)
# meyveler.remove("kavun")  liste içinde olmadığı için hata verdi

# pop()
silenen = meyveler.pop()
print(meyveler)
print(silenen)
silinen = meyveler.pop(1)
print(meyveler)
print(silinen)

# sort()
sayilar = [89, 42, 70, 12, 53, 89]
isimler = ["Zeynep", "Eren", "Fatma", "Muhammed", "Kerem"]
sayilar.sort()
print(sayilar)
sayilar.sort(reverse=True)
print(sayilar)
isimler.sort()
print(isimler)
isimler.sort(reverse=True)
print(isimler)

# count()
isim = "Eren Mustafa Özdal"
karakterler = [x for x in isim.lower()]
print(karakterler)
print(karakterler.count("e"))
print(karakterler.count("a"))

# İç içe geçmiş listeler (matris)
ogrenciler = [["Eren", 70, 64, 85], ["Ahmet", 90, 75, 80]]
print(f"{ogrenciler[0][0]} isimli öğrencinin notları: {ogrenciler[0][1:]}")
