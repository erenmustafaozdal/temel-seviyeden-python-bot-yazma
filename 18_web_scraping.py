import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from ayarlar import API_TOKEN

# botu oluşturalım
bot = Bot(token=API_TOKEN)
# gelen komutları yakalamak için dispatcher nesnesi oluşturalım
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_hello(message: types.Message):
    await message.answer("Merhaba, son haberi istiyorsanız /haber komutunu gönderin.")

@dp.message_handler(commands=["haber"])
async def send_news(message: types.Message):
    # get isteği oluşturalım ve cevabı alalım
    response = requests.get("https://teknolojiaihl.meb.k12.tr")

    # cevabı inceleyelim
    await message.reply(f"Durum kodu: {response.status_code}")
    # print(response.text)

    # Gelen yanıtı BeautifulSoup ile ayrıştıralım
    soup = BeautifulSoup(response.content, "html.parser")

    # Sayfa başlığını yazdıralım
    await message.answer(f"Başlık: {soup.title.text}")
    # print(soup.find_all("a"))

    # haberleri alalım
    news = soup.find("div", attrs={"id": "haber_blok"})
    # print(news)

    message_text = "HABERLER\n"
    for report in news.find_all("p"):
        message_text += report.text + "\n"
        print(report.text)

    await message.answer(message_text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
