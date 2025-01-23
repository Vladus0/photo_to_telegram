import telegram
import os
import urllib3 
from dotenv import load_dotenv


load_dotenv()

token = os.environ['TOKEN']

chat_id = "@for_test_t"

bot = telegram.Bot(token=token)
bot.send_photo(chat_id=chat_id, photo=open('imgs/nasa_image0.jpg', 'rb'))
