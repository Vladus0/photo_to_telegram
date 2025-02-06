import telegram
import os
from dotenv import load_dotenv
import time
import random


def main():
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    time = os.environ['DELAY_TIME']

    chat_id = os.environ["TG_CHAT_ID"]

    bot = telegram.Bot(token=token)

    while True:
        for root, dirs, files in os.walk('imgs'):
            random.shuffle(files)
            for img_name in files:
                bot.send_photo(chat_id=chat_id, photo=open(f'imgs/{img_name}', 'rb'))
                time.sleep(5)
        time.sleep(time)   


if __name__=="__main__":
    main()