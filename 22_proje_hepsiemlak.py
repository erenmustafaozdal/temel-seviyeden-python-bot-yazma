import traceback
from modules.log import Log
from modules.hepsiemlak import HepsiEmlak
from modules.excel import Excel
from db.model.listings import Listing


# log ayarlarını yapalım
Log("hepsiemlak")

# Excel işlemleri için nesneleri oluşturalım
excel = Excel("./db/hepsiemlak.xlsx")
# Çalışma sayfasını oluşturalım
listing_sheet = Listing(excel.wb)

# HepsiEmlak nesnesi oluştur ve arama yap
he = HepsiEmlak()
he.set_location("Osmaniye")
# he.set_category("Konut")
# he.set_house_types(["Daire", "Villa"])
# he.set_price(1000000, 2000000)
# he.set_square_meters(150, 200)
# he.set_room_types(["3+1", "4+1"])
try:
    results = he.search()
except Exception as e:
    he.driver.save_screenshot("./logs/error.png")
    he.logger.error(
        f"İlan arama sırasında hata oluştu: {traceback.format_exc()}")
    results = []

for result in results:
    listing_sheet.insert(result.__dict__)

excel.save()
