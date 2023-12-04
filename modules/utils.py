import logging
import requests
from typing import Union


logger = logging.getLogger(__name__)


def download(src: str, dest: str) -> Union[str, None]:
    """
    İnternetten bir kaynağın indirilmesini ve hedefe kaydedilmesini sağlar

    Args:
        src (str): kaynak adresi
        dest (str): yerel hedef yolu

    Returns:
        str: _description_
    """
    try:
        response = requests.get(src)
        if response.status_code == 200:
            with open(dest, "wb") as file:
                file.write(response.content)

            return dest
        else:
            logger.error(f"----- {src} adresinden dosya indirilemedi.")
            return None
    except Exception as e:
        logger.error(f"----- Dosya indirilirken hata oluştu: {e}")
        return None
