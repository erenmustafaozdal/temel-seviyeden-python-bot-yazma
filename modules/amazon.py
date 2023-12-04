import os
import logging
from datetime import datetime
from modules.browser import Browser
from modules.utils import download
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


logger = logging.getLogger(__name__)


class Amazon:

    URL = "https://amazon.com.tr"
    IMAGES_DIR = "./images/amazon"

    # SEÇİCİLER
    # arama kutucuğu
    search_box_id = "twotabsearchtextbox"
    # çerez kabul et butonu
    cookie_btn_id = "sp-cc-accept"
    # arama sonucundaki ürünler
    products_xpath = "//div[@data-component-type='s-search-result']"
    # ürün fiyat bilgileri
    price_whole = "a-price-whole"
    price_fraction = "a-price-fraction"

    def __init__(self) -> None:
        # görselleri indireceğimiz klasör yoksa oluşturalım
        if not os.path.exists(self.IMAGES_DIR):
            os.makedirs(self.IMAGES_DIR)

        # Tarayıcı nesnesini oluşturalım
        self.driver = Browser().get()

        # sınıf genelinde kullanılacak bir bekleme nesnesi oluşturulur
        self.wait = WebDriverWait(self.driver, 10)

        # amazon sayfasına gidelim
        self.driver.get("https://amazon.com.tr")
        self.load_page()

        # eğer varsa çerezleri kabul et
        self.accept_cookie()

    def load_page(self):
        while True:
            try:
                self.wait.until(ec.visibility_of_element_located(
                    (By.ID, self.search_box_id)
                ))
                break
            except TimeoutException:
                logger.error(
                    f"Sayfa yüklenirken zaman aşımı oldu: {self.driver.current_url}")
                self.driver.refresh()

    def accept_cookie(self):
        try:
            self.driver.find_element(By.ID, self.cookie_btn_id).click()
        except NoSuchElementException:
            logger.info(
                "Çerezleri kabul et tuşu bulunamadı veya gerekli değil.")

    def search_products(self, query) -> list:
        logger.info(f"Arama sorgusu: {query}")

        self.driver.find_element(
            By.ID, self.search_box_id).send_keys(query + Keys.ENTER)

        self.load_page()

        try:
            products = self.wait.until(ec.visibility_of_all_elements_located(
                (By.XPATH, self.products_xpath)
            ))
            return products
        except TimeoutException:
            logger.error("Ürünler yüklenirken zaman aşımı oldu.")
            return []

    def process_product(self, product: WebElement) -> dict:
        """
        Tek bir ürünün bilgilerini işlenmesi

        Args:
            product (WebElement): Web sitesindeki ürün elemanını temsil eder

        Returns:
            dict: Alınan ürün bilgilerini, tablodaki sütun isimleri anahtarıyla sözlük olarak döndürür
        """
        # ürünün asin bilgisini alalım
        asin = product.get_attribute("data-asin")
        logger.info(f"{asin} ASIN'li ürün bilgileri alınıyor...")

        # ürünün adını alalım
        try:
            name = product.find_element(By.TAG_NAME, "h2").text
            logger.info(f"----- Ürün adı: {name}")
        except NoSuchElementException:
            name = ""
            logger.error(f"----- {asin} ASIN'li üründe ürün adı bulunamadı.")

        # ürünün resim linkini (<img src="">) alalım
        try:
            src = product.find_element(By.TAG_NAME, "img").get_attribute("src")
            dest_path = f"{self.IMAGES_DIR}/{asin}.jpg"
            result = download(src, dest_path)

            # eğer hedef yol döndüyse
            if result:
                image = f'=HYPERLINK("{os.getcwd()}/{dest_path}", "GÖRSEL")'
                logger.info(
                    f"----- `{src}` adresindeki görsel `{dest_path}` adresinde kaydedildi.")
            else:
                image = ""
        except NoSuchElementException:
            image = ""
            logger.error(f"----- {asin} ASIN'li ürünün resmi indirilemedi.")

        # ürünün fiyatını alalım
        try:
            lira = product.find_element(
                By.CLASS_NAME, self.price_whole).text.replace(".", "")
            kurus = product.find_element(
                By.CLASS_NAME, self.price_fraction).text
            price = float(f"{lira}.{kurus}")
            logger.info(f"----- Ürünün fiyatı: {price}")
        except:
            price = ""
            logger.error(f"----- {asin} ASIN'li ürünün fiyatı bulunamadı.")

        return {
            "TARİH": datetime.now(),
            "ASIN": asin,
            "AD": name,
            "GÖRSEL": image,
            "FİYAT": price,
        }
