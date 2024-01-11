import time
import logging
from modules.log import Log
from modules.hepsiemlak import HepsiEmlak


# log ayarlarını yapalım
Log("hepsiemlak")
logger = logging.getLogger(__name__)

# HepsiEmlak nesnesi oluştur ve arama yap
s = HepsiEmlak()
s.search(categories="Konut,Satılık,Daire")

time.sleep(5)
