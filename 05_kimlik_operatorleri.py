# Kimlik operatörleri: is, is not

a = [1, 2, 3]
b = a

# is Operatörü
print(b is a)  # Çıktı: True
c = [1, 2, 3]
print(c is a)  # Çıktı: False
print(c == a)  # Çıktı: True

# is not Operatörü
print(b is not a)  # Çıktı: False
print(c is not a)  # Çıktı: True
