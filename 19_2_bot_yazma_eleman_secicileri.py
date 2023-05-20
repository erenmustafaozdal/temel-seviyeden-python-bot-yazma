from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# tarayıcıyı tek satırda oluşturalım
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# internet sayfamıza gidelim
driver.get("https://teknolojiaihl.meb.k12.tr")

# id ile web sayfasındaki bir elemanı seçelim
element = driver.find_element(By.ID, "araTextBox")

# elemanın bazı değerlerini yazdıralım
print(element.text)
print(element.id)

# elemanın öz niteliğini alalım
print(element.get_attribute("type"))

# elemanın ekran görüntüsünü alalım
element.screenshot("./images/taihl_arama.png")

# input alanına yazı yazalım
element.send_keys("merhaba dünya!")

# input alanını temizleyelim
element.clear()
element.send_keys("teknoloji")

# name attribute ile web sayfasındaki bir elemanı seçelim
driver.find_element(By.NAME, "sa2").click()  # yeni sekmede açıyor

# açılan sekmeye geçelim
tabs = driver.window_handles
driver.switch_to.window(tabs[-1])  # açılan son sekmeye geçildi

# tag name ile web sayfasındaki elemanları seçelim
h3s = driver.find_elements(By.TAG_NAME, "h3")
print(h3s)
for h3 in h3s:
    print(h3.text)

# tekrar ilk sekmeye geçelim
driver.switch_to.window(tabs[0])

# class name ile web sayfasındaki elemanları seçelim
print(driver.find_elements(By.CLASS_NAME, "menu-item"))

# css selector ile web sayfasındaki elemanları seçelim
menu_items = driver.find_elements(By.CSS_SELECTOR, "li.menu-item")
for menu_item in menu_items:
    print(menu_item.get_attribute("class"))
    if "dropdown" in menu_item.get_attribute("class"):
        menu_item.click()

    # xpath ile web sayfasındaki elemanı seçelim
    # XPATH kopya kağıdı: https://devhints.io/xpath
    try:
        menu_link = menu_item.find_element(By.XPATH, "./a[@href!='#' and @href!='']")
        print(menu_link.get_attribute("href"))
    except:
        pass


# link text ile web sayfasındaki elemanı seçelim
mebim_link = driver.find_element(By.LINK_TEXT, "444 0 MEB")

# ActionChains ile işlemler yapalım
ActionChains(driver).key_down(Keys.CONTROL).click(mebim_link).key_up(Keys.CONTROL).perform()
sleep(3)

# partial link text ile web sayfasındaki elemanları seçelim
links = driver.find_elements(By.PARTIAL_LINK_TEXT, "MEB")
for link in links:
    print(link.get_attribute("href"))

# tarayıcıyı kapatalım
driver.quit()
