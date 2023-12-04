from datetime import datetime
import logging
import os
import sys


class Log:

    PATH = "./logs"

    def __init__(self, filename: str) -> None:
        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        TODAY_STR = datetime.today().strftime("%Y%m%d")
        logger = logging.getLogger(__name__)

        # eğer klasör yoksa oluştur
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)

        # dosya loglama işleyicisi
        file_handler = logging.FileHandler(
            f"{self.PATH}/{filename}-{TODAY_STR}.log",
            encoding="utf-8",
            mode="a"
        )

        # konsol loglama işleyicisi
        stream_handler = logging.StreamHandler(stream=sys.stdout)

        # log ayarları yapılır
        logging.basicConfig(
            handlers=[file_handler, stream_handler],
            format="%(asctime)s - %(levelname)s - %(name)s: %(message)s",
            level=logging.INFO,
        )

        # ilk log atılır
        logger.info("Log ayarları yapıldı")
