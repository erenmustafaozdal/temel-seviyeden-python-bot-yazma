import re
import logging
from time import sleep
from random import randint
from datetime import datetime
from tqdm import tqdm
from modules.bypass_cloudflare import BypassCloudflare
from modules.browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class HepsiEmlak:

    URL = "https://www.hepsiemlak.com/osmaniye-kiralik"
    # URL = "https://www.hepsiemlak.com/satilik"
    logger = None
    driver = None

    categories = ["Konut", "İşyeri", "Arsa", "Devremülk", "Turistik İşletme"]
    house_types = [
        "Daire",
        "Villa",
        "Müstakil Ev",
        "Prefabrik",
        "Bina",
        "Residence",
        "Bungalov",
        "Yazlık",
        "Köy Evi",
        "Çiftlik Evi",
        "Köşk",
        "Yalı Dairesi",
        "Yalı",
        "Dağ Evi",
        "Loft Daire",
        "Kooperatif"
    ]
    room_types = [
        "Stüdyo",
        "1+1",
        "2+1",
        "3+1",
        "4+1",
        "2",
        "2+2 ve üzeri",
        "3",
        "3+2",
        "3+3 ve üzeri",
        "4",
        "4+2",
        "4+3",
        "4+4 ve üzeri",
        "5",
        "5+1",
        "5+2",
        "5+3",
        "5+4 ve üzeri",
        "6",
        "6+1",
        "6+2",
        "6+3",
        "6+4 ve üzeri",
        "7",
        "7+1",
        "7+2",
        "7+3",
        "7+4 ve üzeri",
        "8",
        "8+1",
        "8+2",
        "8+3",
        "8+4 ve üzeri",
        "9 ve üzeri"
    ]

    # SEÇİCİLER
    content_xpath = "//div[contains(@class, 'list-wrapper')]"
    applied_filter_class = "applied-filters"
    # location
    city_select_xpath = "//section[contains(@class, 'locationCitySec')]/descendant-or-self::div[@class='he-select-base']"
    city_li_xpath = "//li[contains(@class, 'he-select__list-item') and normalize-space()='{city}']"
    county_select_xpath = "//section[contains(@class, 'locationCountySec')]/descendant-or-self::div[@class='he-select-base']"
    county_li_xpath = "//li[contains(@class, 'he-multiselect__list-item') and normalize-space()='{county}']"
    district_select_xpath = "//section[contains(@class, 'locationDistrictSec')]/descendant-or-self::div[@class='he-select-base']"
    district_li_xpath = "//li[contains(@class, 'he-tree-select')]/a[contains(normalize-space(), '{district}')]"
    # category
    category_xpath = "//a[@class='category-main__link' and normalize-space()='{category}']"
    # house_types
    house_type_select_xpath = "//section[contains(@class, 'categorySubSec')]/descendant-or-self::div[@class='custom-select']"
    house_type_li_xpath = "//a[@class='sub-category-link' and normalize-space()='{house_type}']/descendant::span"
    # price
    min_price_id = "priceMin"
    max_price_id = "priceMax"
    # square_meters
    min_square_meters_id = "squareMin"
    max_square_meters_id = "squareMax"
    # room_types
    room_type_select_xpath = "//section[contains(@class, 'roomTypeSec')]/descendant-or-self::div[@class='custom-select']"
    room_type_li_xpath = "//label[@class='md-checkbox' and normalize-space()='{room_type}']/descendant::span"
    listing_link_xpath = "//li[contains(@class,'listing-item')]/descendant::a[@class='card-link']"
    # pagination
    next_page_class = "he-pagination__navigate-text--next"

    def __init__(self) -> None:

        # arama yapmak için query dict verisi
        self.query = {}

        self.browser = Browser(is_headless=True)
        self.driver = self.browser.get()
        self.logger = logging.getLogger(__name__)

        # sınıf genelinde kullanılacak bir bekleme nesnesi oluşturulur
        self.wait = WebDriverWait(self.driver, 10)

    def set_location(self, city, county=None, district=None):
        self.query["location"] = {
            "city": city,
            "county": county,
            "district": district,
        }

    def set_category(self, category):
        if category not in self.categories:
            exit(f"{category} kategorisi bulunamadı")

        self.query["category"] = category

    def set_house_types(self, house_types: list):
        self.query["house_types"] = []

        for house_type in house_types:
            if house_type in self.house_types:
                self.query["house_types"].append(house_type)

    def set_price(self, min_price=None, max_price=None):
        self.query["price"] = {"min": min_price, "max": max_price}

    def set_square_meters(self, min_meters=None, max_meters=None):
        self.query["square_meters"] = {"min": min_meters, "max": max_meters}

    def set_room_types(self, room_types: list):
        self.query["room_types"] = []

        for room_type in room_types:
            if room_type in self.room_types:
                self.query["room_types"].append(room_type)

    def is_page_loaded(self):
        '''
        Waits for page to completely load by comparing current page hash values.
        '''

        def get_page_hash():
            '''
            Returns html dom hash
            '''
            # can find element by either 'html' tag or by the html 'root' id
            dom = self.driver.find_element(
                By.TAG_NAME, "html").get_attribute("innerHTML")
            dom_hash = hash(dom.encode('utf-8'))
            return dom_hash

        page_hash = 'empty'
        page_hash_new = ''

        # comparing old and new page DOM hash together to verify the page is fully loaded
        while page_hash != page_hash_new:
            page_hash = get_page_hash()
            sleep(0.1)
            page_hash_new = get_page_hash()

    def search(self):
        self.driver.get(self.URL)
        self.is_page_loaded()
        self.logger.info("İlan arama işlemi başlatılıyor")

        # filtrelemeler yapılır
        # self.select_location()
        # self.select_category()
        # self.select_house_types()
        # self.write_price()
        # self.write_square_meters()
        # self.select_room_types()
        # button = self.driver.find_element(By.LINK_TEXT, "Ara")
        # self.browser.click(button)
        # self.is_page_loaded()
        # self.logger.info(f"Arama yapıldı. Gezilcek ilanlar: {self.query}")

        # listelemeleri gez
        datas = []
        while True:

            listings = self.driver.find_elements(
                By.XPATH, self.listing_link_xpath)
            self.logger.info(f"Sayfada bulunan ilan sayısı: {len(listings)}")

            for listing in listings:
                # CloudFlare engeline takılmamak için her 50 ilan sonrasında
                # 3-5 dakika rastgele bekle. Çalıştırmalar sonucunda 100-150
                # ilan kontrolü sonrasında CloudFlare'e takılıyor.
                if len(datas) != 0 and len(datas) % 50 == 0:
                    seconds = randint(180, 300)
                    self.logger.info(
                        f"50 ilan tamamlandı. {seconds} saniye bekleniyor.")
                    for i in tqdm(range(seconds), desc="Devam edecek!"):
                        sleep(1)

                self.logger.info(
                    f"{len(datas)+1}. İlan: {listing.get_attribute('title')}")
                # yeni taba geç
                ActionChains(self.driver) \
                    .key_down(Keys.CONTROL) \
                    .click(listing) \
                    .key_up(Keys.CONTROL) \
                    .perform()
                self.driver.switch_to.window(self.driver.window_handles[-1])
                sleep(1)

                # listeleme bilgilerini al
                he_listing = HE_Listing(self)

                datas.append(he_listing)
                # tabı kapat
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[-1])

            try:
                self.driver.find_element(
                    By.CLASS_NAME, self.next_page_class).click()
                self.is_page_loaded()
            except:
                break

        return datas

    def select(self, select_type, value):
        select_el = self.wait.until(ec.element_to_be_clickable(
            (By.XPATH, getattr(self, f"{select_type}_select_xpath"))
        ))
        self.browser.click(select_el)

        xpath = getattr(self, f"{select_type}_li_xpath").format(
            **{select_type: value})
        el = self.wait.until(ec.presence_of_element_located(
            (By.XPATH, xpath)
        ))
        self.browser.click(el)

        # html body'ye tıklayarak seçim alanını kapat
        el = self.driver.find_element(By.CLASS_NAME, self.applied_filter_class)
        self.browser.click(el)

    def select_location(self):
        # eğer location belirlenmemişse dön
        if "location" not in self.query.keys():
            return

        # il seçimi yapılır
        self.select("city", self.query["location"]["city"])

        # eğer varsa ilçe seçimi yapılır
        if self.query["location"]["county"]:
            self.select("county", self.query["location"]["county"])

        # eğer varsa mahalle seçimi yapılır
        if self.query["location"]["district"]:
            self.select("district", self.query["location"]["district"])

    def select_category(self):
        # eğer category belirlenmemişse dön
        if "category" not in self.query.keys():
            return

        xpath = self.category_xpath.format(category=self.query["category"])
        category_el = self.driver.find_element(By.XPATH, xpath)
        input_el = category_el.find_element(By.TAG_NAME, "input")
        is_checked = input_el.get_attribute("checked")

        if is_checked != "true":
            current_url = self.driver.current_url
            self.browser.click(category_el)
            self.wait.until(ec.url_changes(current_url))

    def select_house_types(self):
        # eğer location belirlenmemişse dön
        if "house_types" not in self.query.keys():
            return

        # konut tipleri seçimi yapılır
        for house_type in self.query["house_types"]:
            self.select("house_type", house_type)

    def write_price(self):
        # eğer location belirlenmemişse dön
        if "price" not in self.query.keys():
            return

        # var olan fiyatlar yazılır
        if self.query["price"]["min"]:
            self.driver.find_element(By.ID, self.min_price_id).send_keys(
                self.query["price"]["min"])

        if self.query["price"]["max"]:
            self.driver.find_element(By.ID, self.max_price_id).send_keys(
                self.query["price"]["max"])

    def write_square_meters(self):
        # eğer location belirlenmemişse dön
        if "square_meters" not in self.query.keys():
            return

        # var olan fiyatlar yazılır
        if self.query["square_meters"]["min"]:
            self.driver.find_element(By.ID, self.min_square_meters_id).send_keys(
                self.query["square_meters"]["min"])

        if self.query["square_meters"]["max"]:
            self.driver.find_element(By.ID, self.max_square_meters_id).send_keys(
                self.query["square_meters"]["max"])

    def select_room_types(self):
        # eğer location belirlenmemişse dön
        if "room_types" not in self.query.keys():
            return

        # konut tipleri seçimi yapılır
        for room_type in self.query["room_types"]:
            self.select("room_type", room_type)


class HE_Listing:

    # SEÇİCİLER
    no_xpath = "//span[text()='İlan no']/following-sibling::span"
    price_class = "price"
    city_xpath = "//ul[@class='short-info-list']/li[1]"
    county_xpath = "//ul[@class='short-info-list']/li[2]"
    district_xpath = "//ul[@class='short-info-list']/li[3]"
    update_date_xpath = "//span[text()='Son Güncelleme Tarihi']/following-sibling::span"
    listing_status_xpath = "//span[text()='İlan Durumu']/following-sibling::a"
    house_type_xpath = "//span[text()='Konut Tipi']/following-sibling::span"
    house_shape_xpath = "//span[text()='Konut Şekli']/following-sibling::a"
    room_type_xpath = "//span[text()='Oda + Salon Sayısı']/following-sibling::span"
    m2_xpath = "//span[text()='Brüt / Net M2']/parent::li"
    m2_regex = r'\b(\d+)\s*m2\b'
    floor_of_apartment_xpath = "//span[text()='Bulunduğu Kat']/following-sibling::span"
    floor_of_apartment_regex = r'(\d+).\s*Kat'
    age_xpath = "//span[text()='Bina Yaşı']/following-sibling::span"
    age_regex = r'(\d+)\s*Yaşında'
    heating_type_xpath = "//span[text()='Isınma Tipi']/following-sibling::span"
    floors_xpath = "//span[text()='Kat Sayısı']/following-sibling::span"
    floors_regex = r'(\d+)\s*Katlı'
    credit_eligibility_xpath = "//span[text()='Krediye Uygunluk']/following-sibling::span"
    furnished_xpath = "//span[text()='Eşya Durumu']/following-sibling::span"
    bathrooms_xpath = "//span[text()='Banyo Sayısı']/following-sibling::span"
    building_type_xpath = "//span[text()='Yapı Tipi']/following-sibling::span"
    condition_of_building_xpath = "//span[text()='Yapının Durumu']/following-sibling::span"
    usage_status_xpath = "//span[text()='Kullanım Durumu']/following-sibling::span"
    deed_status_xpath = "//span[text()='Tapu Durumu']/following-sibling::span"
    dues_xpath = "//span[text()='Aidat']/following-sibling::span"
    trade_xpath = "//span[text()='Takas']/following-sibling::span"
    front_xpath = "//span[text()='Cephe']/following-sibling::span"
    authorized_office_xpath = "//span[text()='Yetkili Ofis']/following-sibling::span"
    fuel_type_xpath = "//span[text()='Yakıt Tipi']/following-sibling::span"
    description_class = "description-content"

    def __init__(self, he: HepsiEmlak) -> None:
        self.he = he
        self.he.is_page_loaded()

        # listeleme bilgileri
        self.link = self.get_link()
        self.no = self.get_no()
        self.title = self.get_title()
        self.price = self.get_price()
        self.city, self.county, self.district = self.get_location()
        self.update_date = self.get_update_date()
        self.listing_status = self.get_listing_status()
        self.house_type = self.get_house_type()
        self.house_shape = self.get_house_shape()
        self.room_type = self.get_room_type()
        self.gross_m2, self.net_m2 = self.get_m2s()
        self.floor_of_apartment = self.get_floor_of_apartment()
        self.age = self.get_age()
        self.heating_type = self.get_heating_type()
        self.floors = self.get_floors()
        self.credit_eligibility = self.get_credit_eligibility()
        self.furnished = self.get_furnished()
        self.bathrooms = self.get_bathrooms()
        self.building_type = self.get_building_type()
        self.condition_of_building = self.get_condition_of_building()
        self.usage_status = self.get_usage_status()
        self.deed_status = self.get_deed_status()
        self.dues = self.get_dues()
        self.trade = self.get_trade()
        self.front = self.get_front()
        self.authorized_office = self.get_authorized_office()
        self.fuel_type = self.get_fuel_type()
        self.description = self.get_description()

    def get_link(self):
        link = self.he.driver.current_url
        self.he.logger.info(f"----- LINK: {link}")
        return f'=HYPERLINK("{link}", "LINK")'

    def get_no(self):
        no = self.he.driver.find_element(By.XPATH, self.no_xpath).text
        self.he.logger.info(f"----- No: {no}")
        return no

    def get_title(self):
        title = self.he.driver.find_element(By.TAG_NAME, "h1").text.strip()
        self.he.logger.info(f"----- Başlık: {title}")
        return title

    def get_price(self):
        text = self.he.driver.find_element(
            By.CLASS_NAME, self.price_class).text
        self.he.logger.info(f"----- Fiyat: {text}")
        return float(text.replace('TL', '').replace('.', '').strip())

    def get_location(self):
        city = self.he.driver.find_element(
            By.XPATH, self.city_xpath).text.strip()
        county = self.he.driver.find_element(
            By.XPATH, self.county_xpath).text.strip()
        district = self.he.driver.find_element(
            By.XPATH, self.district_xpath).text.strip()
        self.he.logger.info(f"----- Lokasyon: {city} | {county} | {district}")
        return city, county, district

    def get_update_date(self):
        update_date = self.he.driver.find_element(
            By.XPATH, self.update_date_xpath).text
        self.he.logger.info(f"----- Son Güncelleme Tarihi: {update_date}")
        return datetime.strptime(update_date, "%d-%m-%Y")

    def get_listing_status(self):
        listing_status = self.he.driver.find_element(
            By.XPATH, self.listing_status_xpath).text
        self.he.logger.info(f"----- İlan Durumu: {listing_status}")
        return listing_status

    def get_house_type(self):
        try:
            house_type = self.he.driver.find_element(
                By.XPATH, self.house_type_xpath).text
            self.he.logger.info(f"----- Konut Tipi: {house_type}")
            return house_type
        except:
            self.he.logger.warning("----- 'Konut Tipi' bulunamadı.")
            return None

    def get_house_shape(self):
        try:
            house_shape = self.he.driver.find_element(
                By.XPATH, self.house_shape_xpath).text
            self.he.logger.info(f"----- Konut Şekli: {house_shape}")
            return house_shape
        except:
            self.he.logger.warning("----- 'Konut Şekli' bulunamadı.")
            return None

    def get_room_type(self):
        room_type = self.he.driver.find_element(
            By.XPATH, self.room_type_xpath).text
        self.he.logger.info(f"----- Oda + Salon Sayısı: {room_type}")
        return room_type

    def get_m2s(self):
        text = self.he.driver.find_element(By.XPATH, self.m2_xpath).text
        regex = re.compile(self.m2_regex)
        matches = regex.findall(text)
        if matches:
            gross_m2, net_m2 = map(int, matches)
            self.he.logger.info(f"----- Brüt / Net M2: {gross_m2} / {net_m2}")
            return gross_m2, net_m2

        self.he.logger.warning(
            f"----- 'Brüt / Net M2' eşleşmesi bulunamadı. Text: {text}")
        return None, None

    def get_floor_of_apartment(self):
        try:
            text = self.he.driver.find_element(
                By.XPATH, self.floor_of_apartment_xpath).text
        except:
            self.he.logger.warning(f"----- 'Bulunduğu Kat' bulunamadı.")
            return None

        # eğer bulunduğu kat zeminse "Zemin" verisi oluyor
        if "Zemin" in text:
            floor = 0
            self.he.logger.info(f"----- Bulunduğu Kat: {floor}")
            return floor

        regex = re.compile(self.floor_of_apartment_regex)
        matches = regex.search(text)
        if matches:
            floor = int(matches.group(1))
            self.he.logger.info(f"----- Bulunduğu Kat: {floor}")
            return floor

        self.he.logger.warning(
            f"----- 'Bulunduğu Kat' eşleşmesi bulunamadı. Text: {text}")
        return None

    def get_age(self):
        text = self.he.driver.find_element(By.XPATH, self.age_xpath).text

        # eğer bina sıfırsa "Sıfır Bina" verisi oluyor
        if "Sıfır" in text:
            age = 0
            self.he.logger.info(f"----- Bina Yaşı: {age}")
            return age

        regex = re.compile(self.age_regex)
        matches = regex.search(text)
        if matches:
            age = int(matches.group(1))
            self.he.logger.info(f"----- Bina Yaşı: {age}")
            return age

        self.he.logger.warning(
            f"----- 'Bina Yaşı' eşleşmesi bulunamadı. Text: {text}")
        return None

    def get_heating_type(self):
        heating_type = self.he.driver.find_element(
            By.XPATH, self.heating_type_xpath).text
        self.he.logger.info(f"----- Isınma Tipi: {heating_type}")
        return heating_type

    def get_floors(self):
        text = self.he.driver.find_element(By.XPATH, self.floors_xpath).text
        regex = re.compile(self.floors_regex)
        matches = regex.search(text)
        if matches:
            floors = int(matches.group(1))
            self.he.logger.info(f"----- Kat Sayısı: {floors}")
            return floors

        self.he.logger.warning(
            f"----- 'Kat Sayısı' eşleşmesi bulunamadı. Text: {text}")
        return None

    def get_credit_eligibility(self):
        try:
            credit_eligibility = self.he.driver.find_element(
                By.XPATH, self.credit_eligibility_xpath).text
            self.he.logger.info(
                f"----- Krediye Uygunluk: {credit_eligibility}")
            return credit_eligibility
        except:
            self.he.logger.warning("----- 'Krediye Uygunluk' bulunamadı.")
            return None

    def get_furnished(self):
        try:
            text = self.he.driver.find_element(
                By.XPATH, self.furnished_xpath).text
            self.he.logger.info(f"----- Eşya Durumu: {text}")
            return text
        except:
            self.he.logger.warning("----- 'Eşya Durumu' bulunamadı.")
            return None

    def get_bathrooms(self):
        try:
            text = int(self.he.driver.find_element(
                By.XPATH, self.bathrooms_xpath).text)
            self.he.logger.info(f"----- Banyo Sayısı: {text}")
            return text
        except:
            self.he.logger.warning("----- 'Banyo Sayısı' bulunamadı.")
            return None

    def get_building_type(self):
        try:
            building_type = self.he.driver.find_element(
                By.XPATH, self.building_type_xpath).text
            self.he.logger.info(f"----- Yapı Tipi: {building_type}")
            return building_type
        except:
            self.he.logger.warning("----- 'Yapı Tipi' bulunamadı.")
            return None

    def get_condition_of_building(self):
        try:
            condition_of_building = self.he.driver.find_element(
                By.XPATH, self.condition_of_building_xpath).text
            self.he.logger.info(
                f"----- Yapının Durumu: {condition_of_building}")
            return condition_of_building
        except:
            self.he.logger.warning("----- 'Yapının Durumu' bulunamadı.")
            return None

    def get_usage_status(self):
        try:
            usage_status = self.he.driver.find_element(
                By.XPATH, self.usage_status_xpath).text
            self.he.logger.info(
                f"----- Kullanım Durumu: {usage_status}")
            return usage_status
        except:
            self.he.logger.warning("----- 'Kullanım Durumu' bulunamadı.")
            return None

    def get_deed_status(self):
        try:
            deed_status = self.he.driver.find_element(
                By.XPATH, self.deed_status_xpath).text
            self.he.logger.info(
                f"----- Tapu Durumu: {deed_status}")
            return deed_status
        except:
            self.he.logger.warning("----- 'Tapu Durumu' bulunamadı.")
            return None

    def get_dues(self):
        try:
            dues = self.he.driver.find_element(By.XPATH, self.dues_xpath).text
            self.he.logger.info(
                f"----- Aidat: {dues}")
            return float(dues.replace('TL', '').replace('.', '').strip())
        except:
            self.he.logger.warning("----- 'Aidat' bulunamadı.")
            return None

    def get_trade(self):
        try:
            trade = self.he.driver.find_element(
                By.XPATH, self.trade_xpath).text
            self.he.logger.info(
                f"----- Takas: {trade}")
            return trade
        except:
            self.he.logger.warning("----- 'Takas' bulunamadı.")
            return None

    def get_front(self):
        try:
            front = self.he.driver.find_element(
                By.XPATH, self.front_xpath).text
            self.he.logger.info(
                f"----- Cephe: {front}")
            return front
        except:
            self.he.logger.warning("----- 'Cephe' bulunamadı.")
            return None

    def get_authorized_office(self):
        try:
            authorized_office = self.he.driver.find_element(
                By.XPATH, self.authorized_office_xpath).text
            self.he.logger.info(
                f"----- Yetkili Ofis: {authorized_office}")
            return authorized_office
        except:
            self.he.logger.warning("----- 'Yetkili Ofis' bulunamadı.")
            return None

    def get_fuel_type(self):
        try:
            fuel_type = self.he.driver.find_element(
                By.XPATH, self.fuel_type_xpath).text
            self.he.logger.info(
                f"----- Yakıt Tipi: {fuel_type}")
            return fuel_type
        except:
            self.he.logger.warning("----- 'Yakıt Tipi' bulunamadı.")
            return None

    def get_description(self):
        try:
            description = self.he.driver.find_element(
                By.CLASS_NAME, self.description_class).text
            self.he.logger.info(
                f"----- Açıklama: {description}")
            return description
        except:
            self.he.logger.warning("----- 'Açıklama' bulunamadı.")
            return None
