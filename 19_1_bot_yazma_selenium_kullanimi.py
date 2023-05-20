# selenium webdriver import edilir
from selenium import webdriver

# selenium webdriver içindeki chrome service import edilir
from selenium.webdriver.chrome.service import Service

# chrome webdriver versiyonlarını kontrol edecek ve yönetecek olan
# webdriver manager içindeki ChromeDriverManager import edilir
from webdriver_manager.chrome import ChromeDriverManager

# hızı yavaşlatmak için time sleep import edelim
from time import sleep

# chrome driver yüklenir
chrome_driver = ChromeDriverManager().install()

# chrome service oluşturulur
chrome_service = Service(chrome_driver)

# tarayıcı nesnesi oluşturulur ve tarayıcı çalıştırılır
driver = webdriver.Chrome(service=chrome_service)
sleep(1)

# tarayıcı boyutunu alalım ve yeni boyut verelim
print(driver.get_window_size())
driver.set_window_size(500, 300)
sleep(1)

# tarayıcının pozisyonu alalım ve yeni pozisyon belirleyelim
print(driver.get_window_position())
driver.set_window_position(500, 100)
sleep(1)

# tarayıcıyı tam ekran moduna getirelim
driver.fullscreen_window()
sleep(3)

# tarayıcıyı simge durumuna küçültelim
driver.minimize_window()
sleep(3)

# tarayıcıyı ekranı kapla moduna getirelim
driver.maximize_window()
sleep(3)

# internet sitesine gidelim
driver.get("https://teknolojiaihl.meb.k12.tr")
sleep(3)

# sayfayı yenileyelim
driver.refresh()
sleep(3)

# ekran görüntüsü alalım
driver.save_screenshot("./images/taihl.png")

# yeni bir adrese gidelim
driver.get("https://google.com.tr")

# tarayıcıda geri gidelim
driver.back()
sleep(3)

# taraycıda ileri gidelim
driver.forward()
sleep(3)

# tarayıcıyı tüm işlemler bittikten sonra kapatalım
driver.quit()
