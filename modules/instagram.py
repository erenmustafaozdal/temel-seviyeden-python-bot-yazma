import logging
from modules.browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Instagram:

    URL = "https://www.instagram.com"
    logger = None
    driver = None

    # def __new__(cls, *args, **kwargs):
    #     # driver yoksa oluştur
    #     if not cls.driver:
    #         cls.driver = Browser().get()

    #     # logger yoksa oluştur
    #     if not cls.logger:
    #         cls.logger = logging.getLogger(__name__)
    #     return super().__new__(cls)

    # SEÇİCİLER
    instagram_logo = "//i[@role='img' and @aria-label='Instagram']"
    instagram_logo_2 = "//*[name()='svg' and @role='img' and @aria-label='Instagram']"
    input_username = "//input[@name='username']"
    input_password = "//input[@name='password']"
    login_button = "//button[@type='submit']"

    not_now_button = "//div[normalize-space()='Şimdi değil' and @role='button']"
    not_now_button_2 = "//button[normalize-space()='Şimdi Değil']"

    def __init__(self, username: str = None, password: str = None) -> None:
        self.username = username
        self.password = password
        self.driver = Browser().get()
        self.logger = logging.getLogger(__name__)

        # sınıf genelinde kullanılacak bir bekleme nesnesi oluşturulur
        self.wait = WebDriverWait(self.driver, 10)

    def is_page_loaded(self, current_url=None):
        count = 0
        while True:
            # eğer varolan bir sayfa gönderilirse, sayfa url'si değişti mi kontrol et
            if current_url:
                self.wait.until(ec.url_changes(current_url))

            try:
                self.wait.until(ec.visibility_of_element_located(
                    (By.XPATH, self.instagram_logo)
                ))
                break
            except TimeoutException:
                try:
                    self.wait.until(ec.visibility_of_element_located(
                        (By.XPATH, self.instagram_logo_2)
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

    def login(self):
        self.driver.get(self.URL)
        self.is_page_loaded()

        # ilk form elemanı gelene kadar bekle
        self.wait.until(ec.visibility_of_element_located(
            (By.XPATH, self.input_username)
        )).send_keys(self.username)
        self.driver.find_element(
            By.XPATH, self.input_password).send_keys(self.password)
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.is_page_loaded(self.driver.current_url)

        self.bypass_login_info_save_screen()
        self.bypass_open_notification_screen()

    def bypass_open_notification_screen(self):
        try:
            self.driver.find_element(By.XPATH, self.not_now_button_2).click()
            self.logger.info(
                "Bildirimleri Açma ekranında 'Şimdi değil' tuşuna tıklandı.")
        except NoSuchElementException:
            self.logger.info("Bildirimleri Açma ekranı gelmedi.")

    def bypass_login_info_save_screen(self):
        try:
            self.driver.find_element(By.XPATH, self.not_now_button).click()
            self.logger.info(
                "Giriş bilgileri kaydetme ekranında 'Şimdi değil' tuşuna tıklandı.")
        except NoSuchElementException:
            self.logger.info("Giriş bilgileri kaydetme ekranı gelmedi.")


class IG_Profile(Instagram):

    def go_to_profile(self, username: str = None):
        username = username or self.username
        self.driver.get(f"{self.URL}/{username}")
        self.is_page_loaded()
