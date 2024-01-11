import time
import logging
from modules.log import Log
from modules.sahibinden import Sahibinden


# log ayarlarını yapalım
Log("sahibinden")
logger = logging.getLogger(__name__)

# Sahibinden nesnesi oluştur ve arama yap
s = Sahibinden()
s.search(categories="Konut,Satılık,Daire")

time.sleep(5)
