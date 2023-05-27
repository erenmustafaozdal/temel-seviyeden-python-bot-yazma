from modules.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import logging
import sys

komut_log = logging.StreamHandler(stream=sys.stdout)

logging.basicConfig(
    handlers=[komut_log],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%d-%m-%Y %H:%M:%S"
)

logger = logging.getLogger(__name__)


driver = Browser().get()

# amazon sayfasına gidelim
driver.get("https://amazon.com.tr")

# eğer varsa çerezleri kabul et
try:
    driver.find_element(By.ID, "sp-cc-accept").click()
except:
    logger.error("Çerezleri kabul et tuşu bulunamadı.")

# arama yap
driver.minimize_window()
search = "laptop sırt çantası"  # input("Ne aramak isterseniz? ")
driver.maximize_window()
driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search + Keys.ENTER)

# ürünleri gez
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
for product in products:
    # ürünün id'sini alalım
    id = product.get_attribute("data-asin")
    logger.info(f"{id} ID'li ürün bilgileri alınıyor...")

    # ürünün adını alalım
    name = product.find_element(By.TAG_NAME, "h2").text
    logger.info(f"----- Ürün adı: {name}")


