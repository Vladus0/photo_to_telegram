import telegram
import os
import urllib3 
from dotenv import load_dotenv


load_dotenv()

token = os.environ['TOKEN']

bot = telegram.Bot(token=token)
bot.send_message(text='Hi John!', chat_id="@for_test_t")