from openpyxl import Workbook
from modules.excel import ExcelSheet


class Product(ExcelSheet):

    sheet_name = "ÜRÜNLER"
    column_names = [
        "TARİH",
        "ASIN",
        "AD",
        "GÖRSEL",
        "FİYAT",
    ]

    def __init__(self, wb: Workbook) -> None:
        super().__init__(wb)
