from modules.browser import Browser


driver = Browser(True).get()

# amazon sayfasına gidelim
driver.get("https://amazon.com.tr")
print(driver.current_url)
print(driver.title)
