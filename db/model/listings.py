from modules.excel import ExcelSheet


class Listing(ExcelSheet):

    sheet_name = "İLANLAR"
    column_names = [
        "link",
        "no",
        "title",
        "price",
        "city",
        "county",
        "district",
        "update_date",
        "listing_status",
        "house_type",
        "house_shape",
        "room_type",
        "gross_m2",
        "net_m2",
        "floor_of_apartment",
        "age",
        "heating_type",
        "floors",
        "credit_eligibility",
        "furnished",
        "bathrooms",
        "building_type",
        "condition_of_building",
        "usage_status",
        "deed_status",
        "dues",
        "trade",
        "front",
        "authorized_office",
        "fuel_type",
        "description",
    ]
    column_names_translate = {
        "link": "LINK",
        "no": "No",
        "title": "Başlık",
        "price": "Fiyat",
        "city": "Şehir",
        "county": "İlçe",
        "district": "Mahalle",
        "update_date": "Son Güncelleme Tarihi",
        "listing_status": "İlan Durumu",
        "house_type": "Konut Tipi",
        "house_shape": "Konut Şekli",
        "room_type": "Oda + Salon Sayısı",
        "gross_m2": "Brüt M2",
        "net_m2": "Net M2",
        "floor_of_apartment": "Bulunduğu Kat",
        "age": "Bina Yaşı",
        "heating_type": "Isınma Tipi",
        "floors": "Kat Sayısı",
        "credit_eligibility": "Krediye Uygunluk",
        "furnished": "Eşya Durumu",
        "bathrooms": "Banyo Sayısı",
        "building_type": "Yapı Tipi",
        "condition_of_building": "Yapının Durumu",
        "usage_status": "Kullanım Durumu",
        "deed_status": "Tapu Durumu",
        "dues": "Aidat",
        "trade": "Takas",
        "front": "Cephe",
        "authorized_office": "Yetkili Ofis",
        "fuel_type": "Yakıt Tipi",
        "description": "Açıklama",
    }

    def create_column_names(self, column_names):
        # Sütun başlıklarını ekle
        for i, column in enumerate(column_names, start=1):
            self.sheet.cell(1, i, self.column_names_translate[column])
