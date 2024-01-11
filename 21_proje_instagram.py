import time
from instapy import InstaPy
import logging
from modules.log import Log
from modules.instagram import IG_Profile


# log ayarlarını yapalım
Log("instagram")
logger = logging.getLogger(__name__)

# Instagram nesnesi oluştur ve Instagram'a giriş yap
ig = IG_Profile(username="codevoyager7", password="codevoyager.")
ig.login()
ig.go_to_profile("eren.mustafa.ozdal")

time.sleep(5)


# InstaPy(username="codevoyager7", password="codevoyager.")
