# Bir string oluşturun ve onu tersten yazdırın.
isim = "Eren"
print(isim[3] + isim[2] + isim[1] + isim[0])
print(isim[::-1])

# Bir boolean değişken oluşturun ve onu ekrana yazdırın.
var_mi = True
print(var_mi)

# Bir liste oluşturun ve her bir elemanının karesini alarak yeni bir liste oluşturun.
liste = [1, 2, 3]
liste_yeni = [liste[0]**2, liste[1]**2, liste[2]**2]
print(liste_yeni)

# Bir sözlük oluşturun ve bir anahtar-değer çifti ekleyin.
sozluk = {}
sozluk["isim"] = "Eren"
print(sozluk)

# İki set oluşturun ve bu setlerin kesişimini ve birleşimini hesaplayın.
kume1 = {1, 2, 3, 4}
kume2 = {2, 4, 5, 6}
print(kume1.intersection(kume2))  # kesişim
print(kume1 | kume2)  # birleşim 1. yöntem
print(kume1.union(kume2))  # birleşim 1. yöntem
