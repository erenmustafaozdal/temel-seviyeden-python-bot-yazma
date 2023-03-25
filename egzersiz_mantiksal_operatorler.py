# Kullanıcıdan iki sayı girmesini isteyin ve
# bu sayıların her ikisi de pozitif ise
# "Her iki sayı da pozitiftir." yazdırın.
# Aksi takdirde, "En az bir sayı pozitif değil." yazdırın.
sayi1 = 10  # int(input("1. sayıyı yazın: "))
sayi2 = -5  # int(input("2. sayıyı yazın: "))

if sayi1 > 0 and sayi2 > 0:
    print("Her iki sayı da pozitiftir.")
else:
    print("En az bir sayı pozitif değil.")

# Kullanıcıdan bir kelime girmesini isteyin ve
# kelimenin uzunluğunun 5 karakterden az veya
# kelimenin "hello" olup olmadığını kontrol edin.
# Eğer kelime "hello" ise, "Merhaba!" yazdırın.
# Aksi takdirde, "Merhaba değil!" yazdırın.
kelime = input("Kelime yazın: ")

if len(kelime) < 5 or kelime == 'hello':
    print("Merhaba")
else:
    print("Merhaba değil!")
