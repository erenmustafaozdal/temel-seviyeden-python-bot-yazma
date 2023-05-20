from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    def __init__(self, is_headless=False):
        # chrome ayarlarını alalım ve değiştirelim
        # tüm ayarlar: https://chromedriver.chromium.org/capabilities
        options = webdriver.ChromeOptions()

        # gizli çalışma
        if is_headless:
            options.add_argument("--headless")

        chrome_install = ChromeDriverManager().install()
        chrome_service = Service(chrome_install)
        self.driver = webdriver.Chrome(service=chrome_service, options=options)
        self.driver.maximize_window()

    def get(self):
        return self.driver
