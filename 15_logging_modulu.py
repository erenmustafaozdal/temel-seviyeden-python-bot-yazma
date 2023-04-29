import logging
import os
from datetime import datetime
import sys

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="ornek.log",
#     encoding="utf-8",
#     filemode="w",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )

# loglama klasörü yoksa oluşturalım
klasor = "./logs"
if not os.path.exists(klasor):
    os.mkdir(klasor)

# 2 loglama türü oluşturacağız.
#   1. her güne ayrı log dosyası
#   2. komut istemine log yazma
bugun = datetime.today().strftime("%Y-%m-%d")  # 2023-04-29
dosya_log = logging.FileHandler(f"{klasor}/{bugun}.log", encoding="utf-8", mode="a")
komut_log = logging.StreamHandler(stream=sys.stdout)

logging.basicConfig(
    handlers=[dosya_log, komut_log],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%d-%m-%Y %H:%M:%S"
)

logger = logging.getLogger(__name__)

logger.debug("Geliştiricinin kodlama esnasında kullandığı log seviyesi")
logger.info("Bilgilendirme log seviyesi")
logger.warning("Uyarı log seviyesi")
logger.error("Karşılaşılan hatalar log seviyesi")
logger.critical("Yazılımın çalışmasını en üst düzeyde etkileyecek hata log seviyesi")
