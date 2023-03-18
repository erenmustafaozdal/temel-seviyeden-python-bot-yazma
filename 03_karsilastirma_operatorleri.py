# Eşit mi?
x = 5
y = 10
print(x == y)  # Çıktı: False
print(x == 5)  # Çıktı: True

# Eşit değil mi?
print(x != y)  # Çıktı: True
print(y != 10)  # Çıktı: False

# Küçük mü?
print(x < y)  # Çıktı: True
print(y < x)  # Çıktı: False
print("x + 6 < y :", x + 6 < y)  # Çıktı: False

# Büyük mü?
print("x > y:", x > y)  # Çıktı: False
print("y > x:", y > x)  # Çıktı: True

# Küçük veya eşit mi?
print("x <= y:", x <= y)  # Çıktı: True
print("y <= x:", y <= x)  # Çıktı: False
z = 5
print("z <= x:", z <= x)  # Çıktı: True

# Büyük veya eşit mi?
print("x >= y:", x >= y)  # Çıktı: False
print("y >= x:", y >= x)  # Çıktı: True
print("z >= x:", z >= x)  # Çıktı: True

# farklı veri tipindeki değerler de karşılaştırılabilir
print("'3' == 3:", "3" == 3)  # Çıktı: False
print("'eren' == 'eren':", "eren" == "eren")  # Çıktı: True
print("'Eren Mustafa' > 'Eren':", "Eren Mustafa" > "Eren")  # Çıktı: True
print("Yakup Acar > Yakup Er:", "Yakup Acar" > "Yakup Er")  # Çıktı: False
print("a > z:", "a" > "z")  # Çıktı: False
print("a > Z:", "a" > "Z")  # Çıktı: True
print("A > z:", "A" > "z")  # Çıktı: False

# Neden: ABCD....VYZ abcd...vyz


