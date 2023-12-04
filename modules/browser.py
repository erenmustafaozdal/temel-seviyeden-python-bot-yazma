import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


logger = logging.getLogger(__name__)


class Browser:
    """Tarayıcı nesnesini oluşturan ve ilk ayarlarını yapan
    tarayıcı (browser) nesnesi
    """

    def __init__(self, is_headless: bool = False):
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
        # Tarayıcının konsola otomatik olarak log yazmasını engelle.
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # gizli çalışma
        if is_headless:
            options.add_argument("--headless")
            # Bu ayar, Chrome'un GPU (Grafik İşlem Ünitesi) hızlandırmasını
            # devre dışı bırakır. Genellikle baş ağrısı yaratan grafikle
            # ilgili sorunları önlemek için veya headless modda çalışırken
            # performans iyileştirmeleri için kullanılır.
            options.add_argument("--disable-gpu")

        logger.info("Tarayıcı ayarları yapıldı.")

        chrome_install = ChromeDriverManager().install()
        chrome_service = Service(chrome_install)
        self.driver = webdriver.Chrome(service=chrome_service, options=options)
        logger.info("Tarayıcı çalıştırıldı")

        self.driver.maximize_window()
        logger.info("Tarayıcı ekranı kapladı.")

    def get(self):
        return self.driver
