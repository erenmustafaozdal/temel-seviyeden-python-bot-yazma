# Mantıksal operatörler: and, or, not

a = 3
b = 5
c = 7

# and Operatörü
print(a < b and b < c)  # Çıktı: True
print(a < b and b > c)  # Çıktı: False

# or Operatörü
print(a < b or b < c)  # Çıktı: True
print(a < b or b > c)  # Çıktı: True

# not Operatörü
print(not a > b)  # Çıktı: True
print(not a < b)  # Çıktı: False
