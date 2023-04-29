# HATA TÜRLERİ

# 1. SyntaxError
# if x = 5:
#     print("x, 5'e eşittir.")

# 2. NameError
# print(x)

# 3. TypeError
# print("Sayı: " + 5)

# 4. IndexError
liste = [1, 2, 3]
# print(liste[3])

# 5. KeyError
yaslar = {"Eren": 37, "Zeynep": 6}
# print(yaslar["Mehmet"])

# try ... except BLOKLARI
while True:
    try:
        sayi1 = 6  # int(input("Lütfen 1. sayıyı yazın: "))
        sayi2 = 2  # int(input("Lütfen 2. sayıyı yazın: "))
        break
    except ValueError:
        print("Tam sayı girmelisiniz.")

try:
    bolum = sayi1 / sayi2
    print(f"Bölüm: {bolum}")
except ZeroDivisionError:
    print("Sıfıra bölme hatası oluştu.")


"""
HATA AYIKLAMA TEKNİKLERİ
1. print
2. logging modülü
"""
