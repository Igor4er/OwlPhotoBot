import os
from owl_parser import *
from userbot import app
import random
from dotenv import load_dotenv


URL = 'https://www.gettyimages.com/search/2/image?phrase=owl+photo'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}

load_dotenv()

html = get_html(URL, HEADERS)
if html.status_code != 200:
    print(html.status_code)
    raise IdiNahuyException
owls = parse_owl_images(html)

random_owl_photo = random.choice(owls)

chat_id = int(os.getenv('CHAT_ID'))

with app:
    app.send_photo(chat_id, random_owl_photo)
