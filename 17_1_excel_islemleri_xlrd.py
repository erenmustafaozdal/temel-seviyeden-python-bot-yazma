import xlrd

# Excel dosyasını açalım
calisma_kitabi = xlrd.open_workbook("./veriler/WorldCupPlayers.xls")

# ilk sayfayı seçelim (WorldCupPlayers sayfası/sekmesi)
cs = calisma_kitabi.sheet_by_name("WorldCupPlayers")

# ilk hücrenin değerini yazdıralım
print(cs.cell(0, 0).value)

# satır sayısını yazdıralım
print(cs.nrows)

# sütun sayısını yazdıralım
print(cs.ncols)

# filtreleme yaparak satırları yazdıralım
olaylar = []
for row in cs.get_rows():
    # Oyuncu adı RONALDINHO olanlar
    if row[6].value != "RONALDINHO":
        continue

    if row[8].value:
        olaylar.append(row[8].value)

print(olaylar)
