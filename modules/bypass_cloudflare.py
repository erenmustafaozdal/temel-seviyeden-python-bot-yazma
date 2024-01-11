from selenium.webdriver.remote.webdriver import BaseWebDriver as WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BypassCloudflare:

    # SEÇİCİLER
    cloudflare_checkbox = "//div[@id='challenge-stage']/div/label/input[@type='checkbox']"

    def __init__(self, driver: WebDriver) -> None:
        wait = WebDriverWait(driver, 60)
        wait.until(ec.frame_to_be_available_and_switch_to_it(
            (By.TAG_NAME, "iframe")
        ))
        wait.until(ec.presence_of_element_located(
            (By.XPATH, self.cloudflare_checkbox)
        )).click()
        driver.switch_to.parent_frame()
