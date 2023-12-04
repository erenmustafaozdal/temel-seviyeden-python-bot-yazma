import logging
from modules.log import Log
from modules.excel import Excel
from modules.amazon import Amazon
from db.model.product import Product


# Log ayarları yapılır
Log("amazon-urun-arama")
logger = logging.getLogger(__name__)

# Excel dosyası oluştur
excel = Excel("./db/amazon.xlsx")
# Çalışma sayfasını oluştur
product_sheet = Product(excel.wb)

# arama yap
amazon = Amazon()
amazon.driver.minimize_window()
search = input("Ne aramak isterseniz? ")
amazon.driver.maximize_window()
products = amazon.search_products(search)


# ürünleri gez
for product in products:
    # Excel kayıt işlemleri
    product_sheet.insert(amazon.process_product(product))

excel.save()
amazon.driver.close()
