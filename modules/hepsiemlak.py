import logging
from seleniumbase import Driver
import undetected_chromedriver as uc
from modules.browser import Browser
from modules.bypass_cloudflare import BypassCloudflare
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class HepsiEmlak:

    URL = "https://www.hepsiemlak.com"
    logger = None
    driver = None

    # SEÇİCİLER
    container_id = "container"
    cookie_accept_id = "onetrust-accept-btn-handler"
    discovery_area_xpath = "//div[contains(@class, 'feature-discovery--visible')]"

    def __init__(self) -> None:

        # driver yoksa oluştur
        if not self.driver:
            # self.driver = uc.Chrome()
            # options = uc.ChromeOptions()
            # options.headless = False  # Set headless to False to run in non-headless mode

            # self.driver = uc.Chrome(use_subprocess=True, options=options)
            # self.driver.get(self.URL)
            # import time
            # time.sleep(10)
            # self.driver.maximize_window()
            # self.driver.save_screenshot("datacamp.png")
            # self.driver = Browser().get()
            self.driver = Driver(uc=True)
            self.driver.maximize_window()

        # logger yoksa oluştur
        if not self.logger:
            self.logger = logging.getLogger(__name__)

        # sınıf genelinde kullanılacak bir bekleme nesnesi oluşturulur
        self.wait = WebDriverWait(self.driver, 10)

    def is_page_loaded(self):
        count = 0
        while True:

            try:
                self.wait.until(ec.visibility_of_element_located(
                    (By.ID, self.container_id)
                ))
                break
            except TimeoutException:
                self.logger.error(
                    f"Sayfa yüklenirken zaman aşımı oldu: {self.driver.current_url}")
                self.driver.refresh()

                # limit kontrol edilir
                count += 1
                if count == 3:
                    exit(
                        f"Sayfayı yeniden yükleme limitine ulaşıldı. URL: {self.driver.current_url}")

    def accept_cookie(self):
        self.driver.execute_script(
            "arguments[0].click();",
            self.wait.until(ec.element_to_be_clickable(
                (By.ID, self.cookie_accept_id)
            ))
        )

        try:
            self.wait.until(ec.visibility_of_element_located(
                (By.XPATH, self.discovery_area_xpath)
            )).click()
        except TimeoutException:
            self.logger.info(f"Keşfetme alanı görünmedi.")

    def search(self, categories: str):
        """Sahibinden'de arama yapar

        Args:
            categories (str): virgülle ayrılmış kategori listesi
        """
        self.driver.get(self.URL)

        # CloudFlare geçilir ve Çerezler kabul edilir
        BypassCloudflare(self.driver)
        self.is_page_loaded()
        self.accept_cookie()

        categories = categories.split(",")

        # kategori sayfasına gidilir
        for category in categories:
            self.wait.until(ec.element_to_be_clickable(
                (By.PARTIAL_LINK_TEXT, category)
            )).click()
            self.is_page_loaded
