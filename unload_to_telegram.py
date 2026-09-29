import telegram
import os
from dotenv import load_dotenv
import time
import random
from telegram.request import HTTPXRequest
import asyncio


async def main():
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    timeout = os.environ['DELAY_TIME']

    proxy_url = "socks5://127.0.0.1:10808"
    chat_id = os.environ["TG_CHAT_ID"]
    request = HTTPXRequest(proxy=proxy_url, connect_timeout=15.0, read_timeout=20.0)

    bot = telegram.Bot(request=request, token=token)

    while True:
        for root, dirs, files in os.walk('imgs'):
            random.shuffle(files)
            for img_name in files:
                with open(f'imgs/{img_name}', 'rb') as img:
                    await bot.send_photo(chat_id=chat_id, photo=img)
                time.sleep(5)
        time.sleep(timeout)   


if __name__=="__main__":
    asyncio.run(main())