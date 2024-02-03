import logging
from typing import Union
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import undetected_chromedriver as uc


logger = logging.getLogger(__name__)


class Browser:
    """Tarayıcı nesnesini oluşturan ve ilk ayarlarını yapan
    tarayıcı (browser) nesnesi
    """

    def __init__(
        self,
        is_headless: bool = False,
        proxy: Union[str, None] = None,
        undetected: bool = False
    ):
        """Yapılandırma metodu

        Args:
            is_headless (bool, optional): Tarayıcı gizli mi çalışsın. Defaults to False.
        """
        # Chrome tarayıcısının ayarları için bir 'Options' nesnesi oluşturuluyor.
        # Bu ayarlar, tarayıcının nasıl davranacağını belirler.
        # Tüm ayarlar: https://chromedriver.chromium.org/capabilities
        options = Options()

        """
        Tarayıcı ayarlarına çeşitli argümanlar ekleniyor.
        Bu argümanlar, tarayıcının performansını ve güvenlik ayarlarını etkiler.
        """

        # eğer isteniyorsa proxy işlemi başlat
        # eğer proxy kullanılmayacaksa koruma modunu devre dışı bırak
        # http://free-proxy.cz/en/proxylist/country/TR/all/speed/level1
        if proxy:
            options.add_argument(f"--proxy-server={proxy}")

        # Tarayıcının konsola otomatik olarak log yazmasını engelle.
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Tarayıcının bot olduğunu gizleyecek ayarlar yapılandırması
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')

        # gizli çalışma
        if is_headless:
            options.add_argument("--headless")
            # Bu ayar, Chrome'un GPU (Grafik İşlem Ünitesi) hızlandırmasını
            # devre dışı bırakır. Genellikle baş ağrısı yaratan grafikle
            # ilgili sorunları önlemek için veya headless modda çalışırken
            # performans iyileştirmeleri için kullanılır.
            options.add_argument("--disable-gpu")

        logger.info("Tarayıcı ayarları yapıldı.")

        if not undetected:
            chrome_install = ChromeDriverManager().install()
            chrome_service = Service(chrome_install)
            self.driver = webdriver.Chrome(
                service=chrome_service, options=options)
        else:
            self.driver = uc.Chrome(headless=is_headless)

        logger.info("Tarayıcı çalıştırıldı")

        self.driver.maximize_window()
        logger.info("Tarayıcı ekranı kapladı.")

    def get(self):
        return self.driver

    def click(self, element: WebElement):
        # selenium click ile tıklamayı dene
        try:
            element.click()

        # olmazsa javascript ile tıkla
        except:
            self.driver.execute_script("arguments[0].click();", element)
